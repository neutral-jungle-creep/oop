'''https://stepik.org/lesson/701975/step/8?unit=702076'''
from loguru import logger


class CPU:
    def __init__(self, name, fr):
        logger.info(f'Вызов __init__ у класса {self.__class__.__name__}')
        self.name = name
        self.fr = fr


class Memory:
    def __init__(self, name, volume):
        logger.info(f'Вызов __init__ у класса {self.__class__.__name__}')
        self.name = name
        self.volume = volume


class MotherBoard:
    def __init__(self, name, cpu,  mem_slots, total_mem_slots = 4):
        logger.info(f'Вызов __init__ у класса {self.__class__.__name__}')
        self.name = name
        self.cpu = cpu
        self.mem_slots = mem_slots
        self.total_mem_slots = total_mem_slots

    def get_config(self):
        logger.info(f'Вызов get_config у класса {self.__class__.__name__}')
        return [f'Материнская плата: {self.name}', f'Центральный процессор: {self.cpu.name}, {self.cpu.fr}',
                f'Слотов памяти: {self.total_mem_slots}', f'Память: {self.mem_slots[0].name} - {self.mem_slots[0].volume}; '
                                                          f'{self.mem_slots[1].name} - {self.mem_slots[1].volume}']

cpu = CPU('asus', 1333)
memory1, memory2 = Memory('Kingstone', 4000), Memory('Kingstone', 2000)
mb = MotherBoard('Asus', cpu, [memory1, memory2])
print(mb.get_config())