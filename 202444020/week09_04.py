# week09_03.py

data2 = [
        [1,2,3],
        [10,20],
        [11,12,13,14]
        ]

data3 = {
    "김인하" : [1,2],
    "이인하" : [10,20,30,40,50,60,70],
    "송인하" : [11,12,13,14]
    }


def analyze_list(datas):
    for i,v in enumerate(datas):
        print(f"{i+1}번째 : ",end="")
        for j in range(len(v)):
            print(f"[{j}]{v[j]} ",end="")
        print()
        print(f"sum {sum(v)}")
        print(f"max {max(v)}")
        print(f"min {min(v)}")
        print(f"avg {sum(v)/len(v)}")


def analyze_dict(datas):
    for k in datas:
        print(f"{k} : ",end="")
        for i,val in enumerate(datas[k]):
            print(f"[{i}]{val} ",end="")
        print()
        print("sum", sum(datas[k]))
        print("max", max(datas[k]))
        print("min", min(datas[k]))
        print("avg", sum(datas[k])/len(datas[k]))


def analyze_score(datas):
    if isinstance(datas,list):
        analyze_list(datas)
    elif isinstance(datas, dict):
        analyze_dict(datas)
    else:
        print("판독불가")

analyze_list(data2)
analyze_dict(data3)
analyze_score(data2)
