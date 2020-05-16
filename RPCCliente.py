import xmlrpc.client
import datetime
s = xmlrpc.client.ServerProxy('http://localhost:8000')

def ingresaDatos():
    print("Introduce numero x")
    x = int(input())
    print("Introduce numero y")
    y = int(input())
    return x, y

def opciones(opc):
    x, y = ingresaDatos()
    if opc == 1:
        print(s.add(x, y))
    else:
        if opc == 2:
            print(s.rest(x, y))
        else:
            if opc == 3:
                print(s.mul(x, y))
            else:
                if opc == 4:
                    print(s.div(x, y))

def Calc_menu():
    ciclo = -1
    while ciclo != 0:
        print("1-Suma \n2-Resta \n3-Multiplicacion \n4-Division")
        ciclo = int(input())
        if ciclo != 0:
            opciones(ciclo)

Calc_menu()
print("Adios!")
data = [
    ('datetime', datetime.datetime.now()),
    ('integer', 1),
    ('float', 2.5),
    ('string', 'some text'),
    ('boolean', True),
    ('array', ['a', 'list']),
    ('array', ('a', 'tuple')),
    ('structure', {'a': 'dictionary'}),
]

for t, v in data:
    as_string, type_name, value = s.show_type(v)
    print('{:<12}: {}'.format(t, as_string))
    print('{:12}  {}'.format('', type_name))
    print('{:12}  {}'.format('', value))

# Print list of available methods
print(s.system.listMethods())