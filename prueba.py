db = [{'dato1': 1 , 'dato2': 2 , 'dato3':3},{'dato1': 4 , 'dato': 5 , 'dato3':6},{'dato1': 7 , 'dato2': 8 , 'dato3':9}]
dic = {}
dic2 = {}
lista = []



for i in db:
    dic = i
    print(dic)
    #for a in dic.values():
    for dia, codigos in i.items():
        dic2 = dia, codigos
        print(dic2)
        if dia == 'dato3':
            lista.append(codigos)
        else:
            continue
print(lista)








