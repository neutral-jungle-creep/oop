'''https://stepik.org/lesson/701973/step/8?unit=702074'''


class Dictionary:
    rus = 'Питон'
    eng = 'Python'


print(getattr(Dictionary, 'rus_word', False))