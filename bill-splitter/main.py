import random

num_people = int(input("Enter the number of friends joining (including you):\n"))

if num_people < 1:
    print("No one is joining for the party")
else:
    value_by_person = {}
    print("\nEnter the name of every friend (including you), each on a new line:")
    for itr in range(num_people):
        current_name = input()
        value_by_person[current_name] = 0

    total_bill = float(input("\nEnter the total bill value:\n"))
    lucky = input("\nDo you want to use the \"Who is lucky?\" feature? Write Yes/No:\n").lower()

    random_name = random.choice(list(value_by_person.keys()))
    if lucky == "yes":
        print(f"\n{random_name} is the lucky one!")
        num_people -= 1
    else:
        print("\nNo one is going to be lucky")

    divided_bill = round(total_bill / num_people, 2)
    for name in value_by_person:
        if name == random_name and lucky == "yes":
            value_by_person[name] = 0
        else:
            value_by_person[name] = divided_bill

    print(f"\n{value_by_person}")
