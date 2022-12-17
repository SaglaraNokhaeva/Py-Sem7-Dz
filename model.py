data = open('справочник.txt','r',encoding='UTF-8')
guide =[]
for s in data.readlines():
    guide.append(s) 

data.close()
print(guide)

a=bool(input("Добавить новый контракт (True or False)?"))
if a==True:
    guide =[]
    data1 = open('справочник.txt','a',encoding='UTF-8')
    s1=input("Введите Фамилию: ")
    guide.append(s1)
    s1=input("Введите Имя: ")
    guide.append(s1)
    s1=input("Введите Телефон: ")
    guide.append(s1)
    s1=input("Введите Описание: ")
    guide.append(s1)
    data1.write("\n")
    data1.write("\n".join(guide))
    
print(guide)
data1.close()
