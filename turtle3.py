# turtle1.py

from turtle import *
shape("turtle") #カメの登場
col = ["orange","limegreen","gold","plum","tomato"]
for i in range(5):
    color(col[i])
    circle(50) 
    left(65)
done() #おしまい
