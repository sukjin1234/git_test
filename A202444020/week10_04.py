# week10_04.py

myFile = "C:\\A202444020\\yoonseokjin_02.txt"

#전통적인 형태
f = open(myFile, 'r')
pass 
f.close()

#우리를 믿지 않는 형태 (with 끝나면 자동으로 close)
with open(myFile,'r') as f:
    pass
