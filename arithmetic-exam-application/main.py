from random import randint, choice
from os.path import isfile


class IncorrectFormatError(Exception):
    def __str__(self):
        return "Wrong format! Try again."


def set_expression():
    first_num = randint(2, 9)
    second_num = randint(2, 9)
    operator = choice(["*", "+", "-"])

    expression_list = [str(first_num), operator, str(second_num)]
    cur_expression = " ".join(expression_list)

    return cur_expression


def set_integer():
    return randint(11, 29)


def validate_answer(answer, difficulty_level):
    temp = answer.lstrip("-")
    if difficulty_level in (1, "one"):
        temp = answer.lstrip("-")
    try:
        if temp.isdigit():
            return True
        else:
            raise IncorrectFormatError
    except IncorrectFormatError as err:
        return err


def get_value(difficulty_level):
    if difficulty_level in ("1", "one"):
        value = set_expression()

    else:
        value = set_integer()
    return value


def get_level(difficulty_level):
    if difficulty_level in ("1", "one"):
        return 1
    else:
        return 2


def get_description(difficulty_level):
    if difficulty_level == 1:
        return "simple operations with numbers 2-9"
    else:
        return "integral squares of 11-29"


def main():
    while True:
        level = input(("""Which level do you want? Enter a number:
    1 - simple operations with numbers 2-9
    2 - integral squares of 11-29\n"""))
        if level not in ("1", "2", "one", "two"):
            print("Incorrect format.")
        else:
            break

    used_values = []
    grade = 0
    for _ in range(5):

        cur_value = get_value(level)
        while cur_value in used_values:
            cur_value = get_value(level)
            used_values.append(cur_value)
        print(cur_value)

        while True:
            user_answer = input()

            if validate_answer(user_answer, level) is not True:
                print(validate_answer(user_answer, level))
            else:

                if get_level(level) == 1 and eval(cur_value) == float(user_answer):
                    # TODO: create method to automatically check chosen level and its conditions
                    print("Right!")
                    grade += 1
                elif get_level(level) == 2 and cur_value ** 2 == float(user_answer):
                    print("Right!")
                    grade += 1
                else:
                    print("Wrong!")
                break

    print(f"Your mark is {grade}/5.", end=" ")
    save = input("Would you like to save the result? Enter yes or no.\n").lower()
    if save in "yes":
        if isfile("./results.txt"):
            mode = "a"
        else:
            mode = "w"
        name = input("What is your name?\n")
        with open("results.txt", mode) as results_file:
            results_file.write(f"{name}: {grade}/5 in level {level} ({get_description(get_level(level))}).")

        print("The results are saved in \"results.txt\".")


if __name__ == "__main__":
    main()
