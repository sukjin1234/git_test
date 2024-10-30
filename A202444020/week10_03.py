# week10_03.py
myFile = "C:\\A202444020\\yoonseokjin_02.txt"

f = open(myFile, 'r')

#type1
#d = f.read()
#print(d)

#type2
'''
while True:
    d = f.readline()
    if not d:
        break
    print(d.strip())
'''
#type3

d = f.readlines()
for i in d:
    print(i.strip())



f.close()
