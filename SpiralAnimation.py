import turtle
from random import randint 

pen=turtle.Turtle()

turtle.bgcolor("black")

wid=5
height=7

dot_dist=25

pen.penup()
colours=["white","yellow","brown","red","blue","green","orange","cyan","violet","grey"]

pen.setpos(-250,250)

def spiral(m,n):
  k=0 
  l=0 # start index of row and col
  f=0
  pen.color("white")
  col=randint(0,10)
  pen.color(colours[col])
  
  while(k<m and l<n):
    if f==1:
        pen.right(90)

    #for first row 
    for i in range(l,n):
      pen.dot()
      pen.forward(dot_dist)
      #for last col
    k+=1
    f=1

    pen.right(90)
    col=randint(0,10)
    pen.color(colours[col])
    for i in range(k,m):
      pen.dot()
      pen.forward(dot_dist)
    n-=1
    pen.right(90)
    col=randint(0,10)
    pen.color(colours[col])
    if k<m:
      for i in range(n-1,l-1,-1):
        pen.dot()
        pen.forward(dot_dist)
      m-=1
      pen.right(90)
      col=randint(0,10)
    pen.color(colours[col])
    if l<n:
      for i in range(m-1,k-1,-1):
        pen.dot()
        pen.forward(dot_dist)
      l+=1



spiral(20,20)

turtle.done()
