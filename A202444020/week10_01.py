# week10_01.py

myFile = "C:\\A202444020\\yoonseokjin.txt"

#열기
#f = open(myFile,'w') # 쓰기모드
f = open(myFile,'a') # 추가모드
#쓰기/읽기
f.write("윤석진\n")


#닫기
f.close()

f = open(myFile, 'r') # 읽기모드
print(f.read())
f.close()

