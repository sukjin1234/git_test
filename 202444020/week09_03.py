# week09_03.py

data1 = [1,2,3,4]

summary = sum(data1)
maximum = max(data1)
minimum = min(data1)
average = summary/len(data1)

print(summary)
print(maximum)
print(minimum)
print(average)

print("-"*30)

for i in data1:
    print(i)

print("-"*30)

for i in range(len(data1)):
    print(i)

print("-"*30)

for i in range(len(data1)):
    print(f"data1[{i}]:{data1[i]}")

print("-"*30)

for i in enumerate(data1): #i = (idx, value)
    print(f"data1[{i[0]}]:{i[1]}")

print("-"*30)

for i,v in enumerate(data1): #(idx, value)
    print(f"data1[{i}]:{v}")

data2 = [
        [1,2,3],
        [10,20],
        [11,12,13,14]
        ]

print("-"*30)

for v in data2:
    print(v)

print("-"*30)

for v in data2:
    print(f"sum {sum(v)}")
    print(f"max {max(v)}")
    print(f"min {min(v)}")
    print(f"avg {sum(v)/len(v)}")

print("-"*30)

for i,v in enumerate(data2):
    print(f"{i+1}번째 : {v}")
    print(f"sum {sum(v)}")
    print(f"max {max(v)}")
    print(f"min {min(v)}")
    print(f"avg {sum(v)/len(v)}")

print("최종-"*30)

for i,v in enumerate(data2):
    print(f"{i+1}번째 : ",end="")
    for j in range(len(v)):
        print(f"[{j}]{v[j]} ",end="")
    print()
    print(f"sum {sum(v)}")
    print(f"max {max(v)}")
    print(f"min {min(v)}")
    print(f"avg {sum(v)/len(v)}")


data3 = {
    "김인하" : [1,2],
    "이인하" : [10,20,30,40,50,60,70],
    "송인하" : [11,12,13,14]
    }
print("-"*30)

for k in data3:
    print(k)

print("-"*30)

for k in data3:
    print(data3[k])

print("-"*30)

for k in data3:
    print(f"{k} : {data3[k]}")

print("최종-"*30)

for k in data3:
    print(f"{k} : ",end="")
    for i,val in enumerate(data3[k]):
        print(f"[{i}]{val} ",end="")
    print()
    print("sum", sum(data3[k]))
    print("max", max(data3[k]))
    print("min", min(data3[k]))
    print("avg", sum(data3[k])/len(data3[k]))
