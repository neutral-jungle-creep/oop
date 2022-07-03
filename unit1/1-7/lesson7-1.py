'''https://stepik.org/lesson/701978/step/7?unit=702079'''
from loguru import logger


class Factory:
    @staticmethod
    def build_sequence():
        logger.info(f'Вызов build_sequence')
        return []

    @staticmethod
    def build_number(string):
        logger.info(f'Вызов build_number')
        return int(string)


class Loader:
    @staticmethod
    def parse_format(string, factory):
        seq = factory.build_sequence()
        for sub in string.split(","):
            item = factory.build_number(sub)
            seq.append(item)

        return seq


res = Loader.parse_format("1, 2, 3, -5, 10", Factory)
logger.info(f'res == {res}, type == {type(res)}')
