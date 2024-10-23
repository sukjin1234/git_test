# week09_02.py

s0 = {1,2,3,3,4,'1'}
s1 = set("1123a")

print(s0)
print(s1)

print(s1 & s0)
print(s1 | s0)
print(s0 - s1)

s0.add('a') #set 요소 추가
print(s0)

s0.update(['a',10])
print(s0)

s0.remove('a')
print(s0)
