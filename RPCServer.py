from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler

# Restrict to a particular path.
class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)

# Creando servidor
with SimpleXMLRPCServer(('localhost', 8000),
                        requestHandler=RequestHandler) as server:
    server.register_introspection_functions()

    # Registramos funciones bajo otro nombre
    def adder_function(x, y):
        return x + y
    server.register_function(adder_function, 'add')

    def quitar_func(x, y):
        return x - y
    server.register_function(quitar_func, 'rest')

    #Registramos una instancia, y po lo tanto todos los metodos de la instancia
    class MyFuncs:
        def mul(self, x, y):
            return x * y

        def div(self, x, y):
            return x / y

        def show_type(self, arg):
            """Illustrates how types are passed in and out of
            server methods.
            Accepts one argument of any type.
            Returns a tuple with string representation of the value,
            the name of the type, and the value itself.
            """
            return (str(arg), str(type(arg)), arg)

    server.register_instance(MyFuncs())

   #Inicio, corremos el servidor
    server.serve_forever()