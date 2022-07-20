'''https://stepik.org/lesson/701978/step/9?unit=702079'''
import re


class CardCheck:

    @staticmethod
    def check_card_number(number):
        return None is not re.match(r'\d{4}-\d{4}-\d{4}-\d{4}', number) and len(number) == 19

    @staticmethod
    def check_name(name):
        return None is not re.match(r'^[0-9A-Z]+\s[0-9A-Z]+$', name) and len(name.split()) == 2


print(is_number := CardCheck.check_card_number("1234-5678-9012-0000"))
print(is_name := CardCheck.check_name("SERGEI BALAKIREV"))
print(is_number2 := CardCheck.check_card_number("12234-5678-9012-0000"))
print(is_name2 := CardCheck.check_name("SERGEI BaLAKIREV"))