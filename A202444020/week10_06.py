# week10_06.py

class Score:
    def __init__(self, k,e,m): # magic method
        self.kor = k
        self.eng = e
        self.mat = m

    def avg(self):
        return (self.kor + self.eng + self.mat)/3
scores3 = Score(1,2,3)
print(scores3.kor, scores3.avg())
scores3.kor = 100
print(scores3.kor, scores3.avg())

'''
scores1 = [10,20,30]
scores2 = {'k':10,'m':20,'e':30}

def average_list(datas): #function
    return sum(datas)/len(datas)
def average_dict(datas): #function
    return sum(datas.values())/len(datas)

print(average_list(scores1))
print(average_dict(scores2))
'''
