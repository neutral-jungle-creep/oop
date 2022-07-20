'''https://stepik.org/lesson/701978/step/11?unit=702079'''
from loguru import logger


class AppStore:
    applications = []

    def add_application(self, app):
        '''Добавление нового приложения в магазин.'''
        logger.info(f'Вызов add_application')
        self.applications.append(app)

    def remove_application(self, app):
        '''Удаление приложения из магазина.'''
        logger.info(f'Вызов remove_application')
        self.applications.remove(app)

    def block_application(self, app):
        '''Блокировка приложения.'''
        logger.info(f'Вызов block_application')
        app.blocked = True

    def total_apps(self):
        '''Возвращает общее число приложений в магазине.'''
        logger.info(f'Вызов total_apps')
        return len(self.applications)


class Application:
    def __init__(self, name, blocked=False):
        self.name = name
        self.blocked = blocked


store = AppStore()
app_youtube = Application("Youtube")
store.add_application(app_youtube)
store.remove_application(app_youtube)
