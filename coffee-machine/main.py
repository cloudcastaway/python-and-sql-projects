class CoffeeMachine:
    
    def __init__(self):
        self.av_water = 400
        self.av_milk = 540
        self.av_beans = 120
        self.av_cups = 9
        self.av_money = 550
        self.ingredient = ''

    def show_state(self):
        print()
        print('The coffee machine has:')
        print(self.av_water, 'of water')
        print(self.av_milk, 'of milk')
        print(self.av_beans, 'of coffee beans')
        print(self.av_cups, 'of disposable cups')
        print(self.av_money, 'of money')
        print()

    def check_resources(self, water, milk, coffee, money, coffee_flavor):

        if self.av_water < water:
            print('Sorry, not enough water!')

        elif self.av_milk < milk:
            print('Sorry, not enough milk!')

        elif self.av_beans < coffee:
            print('Sorry, not enough coffee!')

        else:
            self.av_water -= water
            self.av_milk -= milk
            self.av_beans -= coffee
            self.av_cups -= 1
            self.av_money += money
            print('I have enough resources, making you a ' + coffee_flavor + '!')

    def ing_amount(self, ingredient):
        return int(input(f'Write how many {self.ingredient} do you want to add:\n'))

    def main(self):

        while True:

            action = input('Write action (buy, fill, take, remaining, exit):\n')

            if action == 'buy':
                coffee_choice = input('What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:\n')
                if coffee_choice == 'back':
                    continue
                elif coffee_choice == '1':
                    self.check_resources(250, 0, 16, 4, 'espresso')
                elif coffee_choice == '2':
                    self.check_resources(350, 75, 20, 7, 'latte')
                elif coffee_choice == '3':
                    self.check_resources(200, 100, 12, 6, 'cappuccino')
                    
            elif action == 'fill':
                self.av_water += self.ing_amount('ml of water')
                self.av_milk += self.ing_amount('ml of milk')
                self.av_beans += self.ing_amount('grams of coffee beans')
                self.av_cups += self.ing_amount('disposable cups of coffee')
                
            elif action == 'take':
                print(f'I gave you ${self.av_money}')
                self.av_money = 0
                
            elif action == 'remaining':
                self.show_state()
            
            elif action == 'exit':
                break
            
            else:
                print('Invalid command')
                continue
      
      
run = CoffeeMachine()
run.main()
