# week10_05.py
import os 

myPath = "C:\\A202444020"
myFile = "yoonseokjin_02.txt"

if False == os.path.exists(myPath):
    os.mkdir(myPath) #myPath 폴더가 없으면 생성

myFullFile = myPath + "\\" + myFile

if os.path.exists(myFullFile):
    with open(myFullFile, 'r') as f:
        lines = f.readlines()

        score_list = []
        for line in lines:
            sub_score_list = line.strip().split('|')
            dict_scores = {}

            for sub_score in sub_score_list:
                score = sub_score.split(',')
                dict_scores[score[0]] = int(score[1])

            if dict_scores:
                score_list.append(dict_scores)
        print(score_list)
            
