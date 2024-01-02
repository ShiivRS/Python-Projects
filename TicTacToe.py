import numpy
print("TIC TAC TOE")
board=numpy.array([['-','-','-'],['-','-','-'],['-','-','-']])
p1='x'
p2='o'


def place(sym):
  print(numpy.matrix(board))  #convert array in matrix format
  while(1):
    row=int(input("Enter row(1,2 or 3): "))
    col=int(input("Enter column(1,2 or 3): "))
  #condition for if the position is already occupied
    if row>0 and col>0 and col<4 and row<4 and board[row-1][col-1]: #because we are taking i+1 as input we are indexing from 1 not 0 from the user
      break
    else:
      print("Invalid input,Try again")
  board[row-1][col-1]=sym

def check_rows(s):
  for row in range(3):
    count=0
    for col in range(3):
      if board[row][col]==s:
        count+=1
      if count==3:
        print(s,"WON!")
        return True
      else:
        return False

def check_col(s):
  for col in range(3):
    count=0
    for row in range(3):
      if board[row][col]==s:
        count+=1
      if count==3:
        print(s,"WON!")
        return True
      else:
        return False

def check_dia(s):
  if board[0][2]==board[1][1] and board[1][1]==board[2][0] and board[1][1]==s:
    print(s,"WINS!")
    return True
  elif board[0][0]==board[1][1] and board[1][1]==board[2][2] and board[1][1]==s:
    print(s,"WINS!")
    return True
  else:
    return False

def won(sym):
  check_rows(sym) or check_col(sym) or check_dia(sym)


def play():
  for turn in range(9):
    if(turn%2==0):
      print("x turn")
      place(p1)
      if won(p1):
        break
    else:
      print("o turn")
      place(p2)
      if won(p2):
        break
  if not(won(p1)) and not(won(p2)):
      print("DRAW!")


play()  
