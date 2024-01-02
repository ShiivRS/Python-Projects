import random
from PIL import Image
print("SNAKES AND LADDERS")

# later try using 2 dictionaries 1 for all ladders and one for all snakes and shorten the code

end=100

def board():
    img=Image.open('C:/Users/rsshi/Downloads/snake&ladder.jpg')
    img.show()

def check_ladder(pp):
    if pp==8:
        print("Ladder")
        return 26
    elif pp==21:
        print("Ladder")
        return 82
    elif pp==43:
        print("Ladder")
        return 77
    elif pp==50:
        print("Ladder")
        return 91
    elif pp==54:
        print("Ladder")
        return 93
    elif pp==62:
        print("Ladder")
        return 96
    elif pp==66:
        print("Ladder")
        return 87
    elif pp==88:
        print("Ladder")
        return 100
    else:
        return pp   # when no ladder
def check_snake(pp):
     if pp==44:
        print("Snake")
        return 22
     elif pp==46:
        print("Snake")
        return 5
     elif pp==48:
        print("Snake")
        return 9
     elif pp==52:
        print("Snake")
        return 11
     elif pp==59:
        print("Snake")
        return 7
     elif pp==64:
        print("Snake")
        return 17
     elif pp==69:
        print("Snake")
        return 36
     elif pp==69:
        print("Snake")
        return 33
     elif pp==73:
        print("Snake")
        return 1
     elif pp==83:
        print("Snake")
        return 19 
     elif pp==92:
        print("Snake")
        return 51
     elif pp==95:
        print("Snake")
        return 24
     elif pp==98:
        print("Snake")
        return 28 
     else:
        return pp   # no snake
    

def reached_end(pp):
    if pp==end:
        return True
    else:
        return False
    
    

def play():
    p1=input("Enter player1 name: ")
    p2=input("Enter player2 name: ")
    pp1=0   #player 1 and 2 points are initialized to 0
    pp2=0

    turn =0

    while(1):
        if turn%2==0:
            print(p1,"'s turn")
            ch=int(input("Continue ? 1/0: "))
            if ch==0:
                print(p1," points:",pp1)
                print(p2,"points:",pp2)
                print("Thanks for Playing!")
                break
            else:
                die=random.randint(1,6)
                print("number rolled on die: ",die)
                pp1+=die
                pp1=check_ladder(pp1)
                pp1=check_snake(pp1)

                if pp1>end:
                    pp1=end  #to make sure player doesnt cross the board
                print(p1,"points: ",pp1)

                if reached_end(pp1):
                    print(p1,"Won!")
                    break
        else:
            print(p2,"'s turn")
            ch=int(input("Continue ? 1/0: "))
            if ch==0:
                print(p1," points:",pp1)
                print(p2,"points:",pp2)
                print("Thanks for Playing!")
                break
            else:
                die=random.randint(1,6)
                print("number rolled on die: ",die)
                pp2+=die
                pp2=check_ladder(pp2)
                pp2=check_snake(pp2)

                if pp2>end:
                    pp2=end  #to make sure player doesnt cross the board
                print(p2,"points: ",pp2)

                if reached_end(pp1):
                    print(p2,"Won!")
                    break
        turn +=1
                    
                    
board()
play()
