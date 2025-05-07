import random

class CreditCard:

    @staticmethod
    def calculate_checksum(card_number):
        summ = 0
        for i in range(0, len(card_number), 2):
            number = int(card_number[i]) * 2
            if number > 9:
                number -= 9
            summ += number
        for i in range(1, len(card_number), 2):
            summ += int(card_number[i])
        aux = summ
        return (10 - (summ % 10)) % 10

    @staticmethod
    def gen_card_number():
        card_number =  "400000" + f"{random.randint(0, 999999999):09}"
        checksum = CreditCard.calculate_checksum(card_number)
        return card_number + str(checksum)

    @staticmethod
    def gen_card_pin():
        return f"{random.randint(0, 9999):04}"