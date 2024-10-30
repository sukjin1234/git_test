# week10_02.py
'''
myFile = "C:\\A202444020\\yoonseokjin_01.txt"
scores = {'k' : 10, 'm' : 100, 'e' : 50}
f = open(myFile, "a")

for k, v in scores.items():
    f.write(f"{k}, {v}\n") # write() argument must be str

print(f)
f.close()
'''
'''
myFile = "C:\\A202444020\\yoonseokjin_01.txt"
scores = {}

f = open(myFile, "a")

while True:
    scores['k'] = int(input("kor : "))
    scores['m'] = int(input("mat : "))
    scores['e'] = int(input("eng : "))

    for k, v in scores.items():
        f.write(f"{k}, {v}\n") # write() argument must be str

    if "y" == input("종료(Y/N)").strip().lower():
        break
        
print(f)
f.close()
'''
myFile = "C:\\A202444020\\yoonseokjin_02.txt"
scores = {}

f = open(myFile, "a")

while True:
    scores['k'] = int(input("kor : "))
    scores['m'] = int(input("mat : "))
    scores['e'] = int(input("eng : "))

    data = ""
    for k, v in scores.items():
        if data:
            data += "|"
        data += f"{k}, {v}"
    f.write(f"{data}\n") # write() argument must be str
    
    if "y" == input("종료(Y/N)").strip().lower():
        break
        
print(f)
f.close()
