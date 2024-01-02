import random

print("Rock Paper Scissor Shoot")
print("-----------------------------------------------------------------------")
l=["Rock","Paper","Scissor"]
cont=1
while(cont==1):
  c=int(input("Rock(0), paper(1) or Scissor(2): "))
  x=random.choice(l)
  print(l[c], " vs " , x)
  if l[c]==x:
    print("Draw")
  elif l[c]=="Rock" and x=="Paper":
    print("You lose")
  elif l[c]=="Rock" and x=="Scissor":
    print("You win")
  elif l[c]=="Scissor" and x=="Paper":
    print("You win")
  elif l[c]=="Scissor" and x=="Rock":
    print("You lose")
  elif l[c]=="Paper" and x=="Rock":
    print("You win")
  elif l[c]=="Paper" and x=="Scissor":
    print("You lose")
  cont=int(input("Play again or Quit 1/0: "))
