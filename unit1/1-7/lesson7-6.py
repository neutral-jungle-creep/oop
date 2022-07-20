'''https://stepik.org/lesson/701978/step/12?unit=702079'''
from loguru import logger


class Viber:
    messages = []

    @classmethod
    def add_message(cls, msg):
        '''Добавление нового сообщения в список сообщений.'''
        logger.info(f'Вызов add_message')
        cls.messages.append(msg)

    @classmethod
    def remove_message(cls, msg):
        '''Удаление сообщения из списка.'''
        logger.info(f'Вызов remove_message')
        cls.messages.remove(msg)

    @staticmethod
    def set_like(msg):
        '''Поставить/убрать лайк для сообщения.'''
        logger.info(f'Вызов set_like')
        if msg.fl_like:
            msg.fl_like = False
        else:
            msg.fl_like = True


    @staticmethod
    def show_last_message(num):
        '''Отображение последних сообщений.'''
        logger.info(f'Вызов show_last_message')
        return Viber.messages[num:]

    @staticmethod
    def total_messages():
        '''Возвращает общее число сообщений.'''
        logger.info(f'Вызов total_messages')
        return len(Viber.messages)


class Message:
    def __init__(self, text, fl_like=False):
        self.text = text
        self.fl_like = fl_like


print(Viber.total_messages())
msg = Message("Всем привет!")
Viber.add_message(msg)
Viber.add_message(Message("Это курс по Python ООП."))
Viber.add_message(Message("Что вы о нем думаете?"))
Viber.set_like(msg)
print(Viber.total_messages())
Viber.remove_message(msg)
print(Viber.total_messages())
