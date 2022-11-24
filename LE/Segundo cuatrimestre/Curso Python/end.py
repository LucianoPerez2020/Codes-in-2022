#Si lo uso es para que no haga un salto de linea y siga "escribiendo" en la msima linea.
a, b = 0, 1
while a < 1000:
    print(a, end=',')
    a, b = b, a+b