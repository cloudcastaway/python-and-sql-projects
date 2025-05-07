import sqlite3
import sys
from credit_card import CreditCard


class BankAccount:

    def __init__(self):

        self.conn = sqlite3.connect("card.s3db")
        self.cur = self.conn.cursor()

        self.cur.execute("""
                CREATE TABLE IF NOT EXISTS card (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    number TEXT NOT NULL UNIQUE,
                    pin TEXT NOT NULL,
                    balance INTEGER DEFAULT 0
                );
                """)

    def main_menu(self):
        while True:
            choice = ""
            while choice not in ("1", "2", "0"):
                choice = input("1. Create an account\n2. Log into account\n0. Exit\n")
            if choice == "1":
                self.create_account()
            elif choice == "2":
                self.log_in()
            else:
                print("\nBye!")
                self.conn.close()
                sys.exit()


    def account_menu(self, card_number):
        while True:
            choice = ""
            while choice not in ("1", "2", "3", "4", "5", "0"):
                choice = input("1. Balance\n2. Add income\n3. Do transfer\n4. Close account\n5. Log out\n0. Exit\n")
            if choice == "1":
                self.cur.execute("SELECT balance FROM card WHERE number = ?", (card_number,))
                balance = self.cur.fetchone()[0]
                print(f"Balance: {balance}")
            elif choice == "2":
                self.add_income(card_number)
            elif choice == "3":
                self.do_transfer(card_number)
            elif choice == "4":
                self.close_account(card_number)
                return
            elif choice == "5":
                print("\nYou have successfully logged out!\n")
                return
            else:
                print("\nBye!")
                self.conn.close()
                sys.exit()


    def create_account(self):
        card = CreditCard()
        card_number = card.gen_card_number()
        card_pin = card.gen_card_pin()
        self.cur.execute("INSERT INTO card (number, pin) VALUES (?,?)", (card_number, card_pin))
        self.conn.commit()
        print("\nYour card has been created")
        print(f"Your card number:\n{card_number}")
        print(f"Your card pin:\n{card_pin}\n")


    def log_in(self):
        entered_number = input("\nEnter your card number:\n")
        entered_pin = input("Enter your PIN:\n")
        try:
            self.cur.execute("SELECT pin FROM card WHERE number = ?", (entered_number,))
            found_pin = self.cur.fetchone()[0]
            if found_pin == entered_pin:
                print("\nYou have successfully logged in!\n")
                self.account_menu(entered_number)
            else:
                print("Wrong card number or PIN\n")
        except TypeError:
            print("Wrong card number or PIN\n")


    def add_income(self, card_number):
        income = int(input("\nEnter income:\n"))
        query = "UPDATE card SET balance = balance + ? WHERE number = ?"
        self.cur.execute(query, (income, card_number))
        print("Income was added!")

        self.conn.commit()


    def do_transfer(self, card_number):
        exists_query = """SELECT 1
        WHERE EXISTS (
        SELECT 1
        FROM card
        WHERE number = ?
        );"""

        print("\nTransfer")
        recipient = input("Enter card number:\n")
        self.cur.execute(exists_query, (recipient,))
        exists = self.cur.fetchone()

        if recipient == card_number:
            print("You can't transfer money to the same account!")
        elif not self.is_number_valid(recipient):
            print("Probably you made a mistake in the card number. Please try again!")
        elif exists is None:
            print("Such a card does not exist.")
        else:
            money_to_transfer = float(input("Enter how much money you want to transfer:\n"))
            check_query = "SELECT balance FROM card WHERE number = ?"
            self.cur.execute(check_query, (card_number,))
            balance = self.cur.fetchone()[0]

            if balance < money_to_transfer:
                print("Not enough money!")
            else:
                subtract_query = "UPDATE card SET balance = balance - ? WHERE number = ?"
                add_query = "UPDATE card SET balance = balance + ? WHERE number =?"
                self.cur.execute(subtract_query, (money_to_transfer, card_number))
                self.cur.execute(add_query, (money_to_transfer, recipient))
                print("Success!")

        self.conn.commit()


    @staticmethod
    def is_number_valid(number):
        reversed_number = str(number)[::-1]
        summ = 0
        for i in range(1, len(number), 2):
            summ += int(reversed_number[i]) * 2
            if int(reversed_number[i]) * 2 > 9:
                summ -= 9
        for i in range(0, len(number), 2):
            summ += int(reversed_number[i])
        if summ % 10 == 0:
            return True
        else:
            return False


    def close_account(self, card_number):
        query = "DELETE FROM card WHERE number = ?"
        self.cur.execute(query, (card_number,))

        self.conn.commit()


BankAccount().main_menu()