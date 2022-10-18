import random
import re


class Password:
    UPPER_CASE_LETTER = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
                         'S', 'T', 'U', 'V', 'W', 'X', 'Y']
    LOWER_CASE_LETTER = list(map(lambda letter: letter.lower(), UPPER_CASE_LETTER))
    DIGITS = [str(x) for x in range(0, 10)]
    SYMBOLS = ['`', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '+', '-', '=', '{', '}', '[', ']', ':',
               ';', '|', '\\', '<', '>', '?', ',', '.', '/', '`', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_',
               '+', '-', '=', '{', '}', '[', ']', ':', ';', '|', '<', '>', '?', ',', '.', '/']
    COMBINATION = []
    COMBINATION.extend(UPPER_CASE_LETTER)
    COMBINATION.extend(LOWER_CASE_LETTER)
    COMBINATION.extend(DIGITS)
    COMBINATION.extend(SYMBOLS)

    def __init__(self, password_length, upper=True, lower=True, nums=True, symb=True):
        self.__password_length = password_length
        self.upper = upper
        self.lower = lower
        self.nums = nums
        self.symb = symb
        self.__password = self.password_generate()

    def password_generate(self):
        i = 0
        password = []
        if self.__password_length >= 4:
            if self.upper is True:
                password.append(random.choice(self.UPPER_CASE_LETTER))
                i += 1
            if self.lower is True:
                password.append(random.choice(self.LOWER_CASE_LETTER))
                i += 1
            if self.nums is True:
                password.append(random.choice(self.DIGITS))
                i += 1
            if self.symb is True:
                password.append(random.choice(self.SYMBOLS))
                i += 1
            if self.__password_length >= 4:
                while i < self.__password_length:
                    password.append(random.choice(self.COMBINATION))
                    i += 1
            random.shuffle(password)
        else:
            for i in range(self.__password_length):
                password.append(random.choice(self.COMBINATION))
        return "".join(password)

    def password_validation_regex(self):
        if re.match("^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$%^&*-]).{8,}$", self.__password):
            return "Hasło prawidłowe"
        else:
            return "Hasło nieprawidłowe"

    def password_validation(self):
        """Sprawdzanie validatora"""
        print("*" * 10)
        print(f"Duża litera: {any(sign for sign in self.__password if sign in self.UPPER_CASE_LETTER)}")
        print(f"Mała litera: {any(sign for sign in self.__password if sign in self.LOWER_CASE_LETTER)}")
        print(f"Cyfra: {any(sign for sign in self.__password if sign in self.DIGITS)}")
        print(f"Symbol: {any(sign for sign in self.__password if sign in self.SYMBOLS)}")
        """Koniec"""
        if (
                len(self.__password) >= 8
                and any(sign for sign in self.__password if sign in self.UPPER_CASE_LETTER)
                and any(sign for sign in self.__password if sign in self.LOWER_CASE_LETTER)
                and any(sign for sign in self.__password if sign in self.DIGITS)
                and any(sign for sign in self.__password if sign in self.SYMBOLS)
        ):
            return "Poprawne Hasło"
        else:
            return "Błędne Hasło"


if __name__ == "__main__":
    pas1 = Password(8)
    print(pas1.password_generate())
    print(pas1.password_validation())
    print(pas1.password_validation_regex())
