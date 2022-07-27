'''https://stepik.org/lesson/701983/step/4?unit=702084'''
from loguru import logger


class Clock:
    def __init__(self, time=0):
        self.__time = time

    def set_time(self, tm):
        if Clock.check_time(tm):
            self.__time = tm

    def get_time(self):
        return self.__time

    @staticmethod
    def check_time(tm):
        return isinstance(tm, int) and -1 < tm < 100_001


clock = Clock(4530)
logger.info(clock.get_time())