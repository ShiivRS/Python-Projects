print("Shopping List")
n=1
l=[]
while(n==1):
  #item=input("Enter what you want ")
  l.append(input("Enter what you want "))
  n=int(input("Want to add another item (1/0) "))
l.sort()
print("Your shopping list is:")
for i in l:
    print(i)
