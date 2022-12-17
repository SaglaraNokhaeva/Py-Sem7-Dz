
data = open('справочник.txt','r',encoding='UTF-8')
guide =[]
for s in data.readlines():
    guide.append(s) 

data.close()
print(guide)

a=input("Добавить новый контракт (True or False)?")
if a==True:
    data = open('справочник.txt','a',encoding='UTF-8')
    s1=input("Введите Фамилию")
    guide.append(s1)
    s1=input("Введите Имя")
    guide.append(s1)
    s1=input("Введите Телефон")
    guide.append(s1)
    s1=input("Введите Описание")
    guide.append(s1)
    data.write(guide+'\n')
    data.close()

print(guide)

