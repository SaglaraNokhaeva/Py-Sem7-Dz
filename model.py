data = open('справочник.txt','r',encoding='UTF-8')
guide =[]
for s in data.readlines():
    guide.append(s) 
data.close()
print(guide)

def init (a):
    global flag
    flag=a

def add():
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
        data1.close()
        return guide
        
def exsport_txt():
    data = open('справочник.txt','r',encoding='UTF-8')
    guide =[]
    for s in data.readlines():
        guide.append(s) 
    data1 = open('guide1.txt','a',encoding='UTF-8')
    data1.write("\n".join(guide)) 
    data.close  
    data1.close()

def exsport_csv():
    data = open('справочник.txt','r',encoding='UTF-8')
    guide =[]
    for s in data.readlines():
        guide.append(s) 
    data1 = open('guide1.csv','a',encoding='UTF-8')
    data1.write("\n".join(guide))   
    data.close
    data1.close()
