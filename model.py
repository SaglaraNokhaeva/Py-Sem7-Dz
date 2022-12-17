
data = open('справочник.txt','r',encoding='UTF-8')
guide =[]
for s in data.readlines():
    guide.append(s) 

print(guide)
data.close()
