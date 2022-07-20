'''https://stepik.org/lesson/701978/step/10?unit=702079'''
from loguru import logger


class Video:
    def create(self, name):
        logger.info(f'Вызов create у класса {self.__class__.__name__}')
        self.name = name

    def play(self):
        logger.info(f'Вызов play у класса {self.__class__.__name__}')
        print(f'воспроизведение видео {self.name}')


class YouTube:
    list_video = []

    @classmethod
    def add_video(cls, video):
        cls.list_video.append(video)

    @classmethod
    def play(cls, video_indx):
        return cls.list_video[video_indx].play()


v1 = Video()
v2 = Video()
v1.create('Python')
v2.create('Python ООП')
YouTube.add_video(v1)
YouTube.add_video(v2)
YouTube.play(0)
YouTube.play(1)