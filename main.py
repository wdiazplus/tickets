retiro = int(input('Cuánto deseas retirar \n'))

denominaciones = [50000,20000,10000,5000,2000,1000,500,200,100,50,20,10,5]
text=[]
separator='|'
for i in range(0,12):
    a = retiro//denominaciones[i]
    if a*denominaciones[i]==retiro:
       text1=(f'{denominaciones[i]}x{a}')
       text.append(text1)
       break
    elif a==0:
        pass
    else:
        retiro = retiro - (a*denominaciones[i])
        text2=(f'{denominaciones[i]}x{a}')
        text.append(text2)

print(f'La combinación adecuada será {separator.join(text)}')


