'''https://stepik.org/lesson/701973/step/10?unit=702074'''


class Figure:
    type_fig = 'ellipse'
    color = 'red'


fig1 = Figure()
fig1.start_pt = (10, 5)
fig1.end_pt = (100, 20)
fig1.color = 'blue'
del fig1.color

print(*fig1.__dict__)