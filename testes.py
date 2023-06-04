def calculo_generico(x):
    def caso_1():
        print(x+1)
    
    def caso_2():
        print(x+2)

x = 0

calculo_generico.caso1(x)
calculo_generico.caso2(x)