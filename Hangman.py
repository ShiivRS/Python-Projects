import random
movies=["Tenet","Interstellar","Batman","Oppenheimer","Memento","Prestige"]

def blanks(picked):
  letter=list(picked)
  temp=[]
  for ch in letter:
    if ch==" ":
      temp.append(" ")
    else:
      temp.append("_ ")
  q=''.join(str(y) for y in temp)
  return q

def present(char,picked):
  count=picked.count(char)
  if count==0:
    return False
  else:
    return True

def unlock(new_qn,picked,char):
  refer=list(picked)
  new_qn_list=list(new_qn)
  temp=[]
  for i in range(len(picked)):
    if refer[i]==" " or refer[i]==char :
      temp.append(refer[i])
    else:
      if new_qn_list[i]=="_ ":
        temp.append("_ ")
      else:
        temp.append(refer[i])
  q_n=''.join(str(x) for x in temp)
  return q_n
      
def game():
  p1=input("Enter player 1 name: ")
  p2=input("Enter player 2 name: ")
  pp1=pp2=0 #points for p1 and p2
  turn=0
  cont=1
  while(cont==1):
    if turn%2==0:
      print(p1,"'s turn:",sep="")
      picked=random.choice(movies)
      qn=blanks(picked)
      print(qn)
      new_qn=qn
      notSaid=True
      while(notSaid):
        char=input("Guess the character: ")
        if (present(char,picked)):
          #unlock the character
          new_qn=unlock(new_qn,picked,char)
          print(new_qn)
          done=int(input("Press 1 to guess movie or 0 to continue "))
          if done==1:
            ans=input("Enter movie name");
            if ans==picked:
              print("Correct")
              pp1+=1
              notSet=False
              print(p1,"Score: ",pp1)
            else:
              print("Try again") 
        else:
          print(char,"Not found")
      c=int(input("1 to continue or 0 to quit"))
      if c==0:
            print(p1,"Score: ",pp1)
            print(p2,"Score: ",pp2)
            print("good bye")
            cont=0
    else:
      print(p2,"'s turn:",sep="")
      picked=random.choice(movies)
      qn=blanks(picked)
      print(qn)
      new_qn=qn
      notSaid=True
      while(notSaid):
        char=input("Guess the character: ")
        if (present(char,picked)):
          #unlock a character
          new_qn=unlock(new_qn,picked,char)
          print(new_qn)
          done=int(input("Press 1 to guess movie or 0 to continue "))
          if done==1:
            ans=input("Enter movie name");
            if ans==picked:
              print("Correct")
              pp2+=1
              notSet=False
              print(p2,"Score: ",pp2)
            else:
              print("Try again") 
        else:
          print(char,"Not found")
      c=int(input("1 to continue or 0 to quit"))
      if c==0:
            print(p1,"Score: ",pp1)
            print(p2,"Score: ",pp2)
            print("good")
            cont=0
    turn+=1
    c=int(input("Enter 0 to stop , 1 to continue"))

game()
