"""def cualquier_nombre(*args,**kwargs):
    print(args,kwargs)

cualquier_nombre(12,45,34,56,34,67,pantalon = 'negro',blusa='azul')
"""

def alcance_local():

    global variable1
    variable1 = 50
    print(variable1)
    variable2 = 60

def alcance_global():
    print(variable1)

variable1 = 90


print(variable1,alcance_global(),alcance_local())