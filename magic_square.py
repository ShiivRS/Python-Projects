print("MAGIC SQUARE")

def magic_square(n):
  ms=[]
  for i in range(n):
    l=[]
    for j in range(n):
      l.append(0) #initialize the lis l elements to 0
    ms.append(l) # initializes the entire square to 0

  x=n//2  # doing floor division because index has to be int and not float
  y=n-1    # x and y are the coordinates for the ele

  num=n**2 #the numbers are n*n values in m-arrays
  count=1 #it starts from 1 to n*n no.s

  while(count<=num): #because we need to include the num
    if(x==-1 and y==n): #condn. 4
      y=n-2
      x=0
    else:
      if (y==n):   #when column value is bigger 
        y=0
      if (x<0):  #if row value is smaller
        x=n-1
  
    if(ms[x][y]!=0):
      y=y-2
      x=x+1
      continue #skip current loop code present after this and start again from top
    else:
      ms[x][y]=count
      count+=1
    y+=1
    x-=1

  for i in range(n):
    for j in range(n):
        print(ms[i][j],end=" ")
    print()
  m=n*(n**2+1)//2
  print("Magic sum number is",m)

n=int(input("Enter the dimension: "))
magic_square(n)
