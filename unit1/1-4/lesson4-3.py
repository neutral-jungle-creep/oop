'''https://stepik.org/lesson/701974/step/8?unit=702075'''


import sys


class StreamData:
    def create(self, fields, lst_values):
        if len(fields) != len(lst_values):
            return False
        for i, j in zip(fields, lst_values):
            setattr(self, str(i), j)
        return True


class StreamReader:
    FIELDS = ('id', 'title', 'pages')

    def readlines(self):
        lst_in = list(map(str.strip, sys.stdin.readlines()))  # считывание списка строк из входного потока
        sd = StreamData()
        res = sd.create(self.FIELDS, lst_in)
        return sd, res


data1 = StreamData()
data1.create(['id', 'name', 'comment'], [4, 'Имя', "Какой-то текст"])
print(data1.__dict__)