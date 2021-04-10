def impr_tabla (num):
    lim = 10
    cont = 1
    while cont <= lim:
        result = cont * num
        print("{} x {} = {}".format(num, cont, result))
        cont = cont + 1
impr_tabla(5)
