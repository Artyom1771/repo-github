#номер 1
my_l=[1,'hello',[1,2,3],(1,2,3),{1,2,3,4},{1:3,8:2}]
for i in my_l:
    print(type(i))
# номер 2
lister=list(input('введите список'))
for i in range(1, len(lister), 2):
    lister[i - 1], lister[i]=lister[i],lister[i-1]
print(lister)

#номер3
months=['Winter','Winter','Spring','Spring','Spring','Summer','Summer','Summer','Autumn','Autumn','Autumn','Winter']
month = int(input('Enter month: '))
print(months[month])
 #номер3.2
ms={1:'Winter',2:'Winter',3:'Spring',4:'Spring',5:'Spring',6:'Summer',7:'Summer',8:'Summer',9:'Autumn',10:'Autumn',11:'Autumn',12:'Winter'}
print(ms[int(input('Enter months'))])

#номер 4
ustr=str(input('Введите строку'))
newustr=ustr.split(' ')
num=0
for i in newustr:
    num+=1
    if len(i)>10:
        print(num,':',i[:10])
    else:
        print(num,':',i)


#номер5
my_lister = [7, 5, 3, 3, 2]
unumber=int(input('Введите число'))
my_lister.append(unumber)
print(list(reversed(sorted(my_lister))))