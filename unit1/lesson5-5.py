'''https://stepik.org/lesson/701975/step/7?unit=702076'''
from loguru import logger


class Graph:
    def __init__(self, data):
        logger.info(f'Вызов __init__ у класса {self.__class__.__name__}')
        self.data = data[:]
        self.dt = ' '.join(list(map(lambda i: str(i), data)))
        self.is_show = True

    def set_data(self, data):
        logger.info(f'Вызов set_data у класса {self.__class__.__name__}')
        self.data = data[:]
        self.dt = list(map(lambda i: str(i), data))

    def show_table(self):
        logger.info(f'Вызов show_table у класса {self.__class__.__name__}')
        if self.is_show:
            print(self.dt)
        else:
            print('Отображение данных закрыто')

    def show_graph(self):
        logger.info(f'Вызов show_graph у класса {self.__class__.__name__}')
        if self.is_show:
            print(f'Графическое отображение данных: {self.dt}')
        else:
            print('Отображение данных закрыто')

    def show_bar(self):
        logger.info(f'Вызов show_bar у класса {self.__class__.__name__}')
        if self.is_show:
            print(f'Столбчатая диаграмма: {self.dt}')
        else:
            print('Отображение данных закрыто')

    def set_show(self, fl_show):
        logger.info(f'Вызов set_show у класса {self.__class__.__name__}')
        self.is_show = fl_show


data_graph = list(map(int, input().split()))
gr = Graph(data_graph)
gr.show_bar()
gr.set_show(False)
gr.show_table()