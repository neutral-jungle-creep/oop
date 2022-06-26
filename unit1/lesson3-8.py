'''https://stepik.org/lesson/701973/step/11?unit=702074'''


class Person:
    name = 'Сергей Балакирев'
    job = 'Программист'
    city = 'Москва'


p1 = Person()
print(p1.__dict__.get('job', False))