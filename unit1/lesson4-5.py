'''https://stepik.org/lesson/701974/step/11?unit=702075'''

class Translator:
    dic_words = {}

    def add(self, eng, rus):
        if eng in self.dic_words.keys():
            self.dic_words[eng].append(rus)
        else:
            self.dic_words[eng] = [rus]

    def remove(self, eng):
        del self.dic_words[eng]

    def translate(self, eng):
        return self.dic_words[eng]


tr = Translator()
tr.add('tree', 'дерево')
tr.add('car', 'машина')
tr.add('car', 'автомобиль')
tr.add('leaf', 'лист')
tr.add('river', 'река')
tr.add('go', 'идти')
tr.add('go', 'ехать')
tr.add('go', 'ходить')
tr.add('milk', 'молоко')

tr.remove('car')
print(*tr.translate('go'))
