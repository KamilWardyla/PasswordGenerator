import random
import re


def password_generator(password_length, upper=True, lower=True, nums=True, symb=True):
    upper_case_letter = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
                         'T', 'U', 'V', 'W', 'X', 'Y']
    lower_case_letter = list(map(lambda letter: letter.lower(), upper_case_letter))
    digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['`', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '+', '-', '=', '{', '}', '[', ']', ':', ';',
               '|', '\\', '<', '>', '?', ',', '.', '/', '`', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '+',
               '-', '=', '{', '}', '[', ']', ':', ';', '|', '<', '>', '?', ',', '.', '/']
    combination = []
    combination.extend(upper_case_letter)
    combination.extend(lower_case_letter)
    combination.extend(digits)
    combination.extend(symbols)
    i = 0
    password = []
    if password_length >= 4:
        if upper is True:
            password.append(random.choice(upper_case_letter))
            i += 1
        if lower is True:
            password.append(random.choice(lower_case_letter))
            i += 1
        if nums is True:
            password.append(random.choice(digits))
            i += 1
        if symb is True:
            password.append(random.choice(symbols))
            i += 1
        if password_length >= 4:
            while i < password_length:
                password.append(random.choice(combination))
                i += 1
        random.shuffle(password)
    else:
        for i in range(password_length):
            password.append(random.choice(combination))
    return "".join(password)


new_password = password_generator(8)


class PasswordValidator:
    def __init__(self, password):
        self.__password = password

    def password_validation(self):
        if re.match("^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$%^&*-]).{8,}$", self.__password):
            return f"Hasło prawidłowe"
        else:
            return f"Hasło nieprawidłowe"


pas = PasswordValidator(new_password)
print(pas.password_validation())


class PasswordValidator2:
    def __init__(self, password):
        self.__password = password
        self.__upper_case_letter = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
                                    'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y']
        self.__lower_case_letter = list(map(lambda letter: letter.lower(), self.__upper_case_letter))
        self.__digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        self.__symbols = ['`', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '+', '-', '=', '{', '}', '[', ']', ':',
                   ';',
                   '|', '\\', '<', '>', '?', ',', '.', '/', '`', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_',
                   '+',
                   '-', '=', '{', '}', '[', ']', ':', ';', '|', '<', '>', '?', ',', '.', '/']
        self.__combination = []
        self.__combination.extend(self.__upper_case_letter)
        self.__combination.extend(self.__lower_case_letter)
        self.__combination.extend(self.__digits)
        self.__combination.extend(self.__symbols)

    def password_validation(self):
        print("*" * 10)
        print(f"Duża litera: {any(sign for sign in self.__password if sign in self.__upper_case_letter)}")
        print(f"Mała litera: {any(sign for sign in self.__password if sign in self.__lower_case_letter)}")
        print(f"Cyfra: {any(sign for sign in self.__password if sign in self.__digits)}")
        print(f"Symbol: {any(sign for sign in self.__password if sign in self.__symbols)}")
        if (
                len(self.__password) >= 8
                and any(sign for sign in self.__password if sign in self.__upper_case_letter)
                and any(sign for sign in self.__password if sign in self.__lower_case_letter)
                and any(sign for sign in self.__password if sign in self.__digits)
                and any(sign for sign in self.__password if sign in self.__symbols)
        ):
            return f"Poprawne Hasło"
        else:
            return f"Błędne Hasło"


pas2 = PasswordValidator2(new_password)
pas3 = PasswordValidator2("j#285454")
print(pas2.password_validation())
print(pas3.password_validation())
