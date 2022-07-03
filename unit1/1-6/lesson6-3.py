'''https://stepik.org/lesson/701976/step/9?unit=702077'''
from loguru import logger


TYPE_OS = 1  # 1 - Windows; 2 - Linux


class Dialog:
    obj = None

    def __new__(cls, *args, **kwargs):
        logger.info(f'Вызов функции __new__, TYPE_OS == {TYPE_OS}')
        if TYPE_OS:
            cls.obj = DialogWindows()
            logger.info(f'Создание экземпляра класса {cls.obj.__class__.__name__}')
        else:
            cls.obj = DialogLinux()
            logger.info(f'Создание экземпляра класса {cls.obj.__class__.__name__}')
        setattr(cls.obj, 'name', args)
        return cls.obj


class DialogWindows:
    name_class = "DialogWindows"


class DialogLinux:
    name_class = "DialogLinux"


dlg = Dialog('название')
logger.info(f'{dlg.__class__.__name__}')
