#To rotate 90 degree left when input is 'L'
def rotate90left(direction):
    if direction=='N':
        return 'W'
    elif direction=='S':
        return 'E'
    elif direction=='E':
        return 'N'
    else:
        return 'S'

#To rotate 90 degree right when input is 'R'
def rotate90right(direction):
    if direction=='N':
        return 'E'
    elif direction=='S':
        return 'W'
    elif direction=='E':
        return 'S'
    else:
        return 'N'

#To move forward one grid
def moveingrid(x,y,direction):
    if direction=='N':
        return x,y+1
    elif direction=='S':
        return x,y-1
    elif direction=='E':
        return x+1,y
    else:
        return x-1,y

#Input test case
input_cord=[]
input_str=[]
u_x,u_y=map(int,input().split())
for i in range(2):
    input_cord.append(input())
    input_str.append(input())

#Processing with the input    
for i in range(2):
    l=input_cord[i].split()
    x=int(l[0])
    y=int(l[1])
    d=l[2]
    s=input_str[i]
    n=0
    flag=False
    while not flag and n<len(s):
        i=s[n]
        if(x<0 or x>u_x or y<0 or y>u_x):
            flag=True
        elif i=='L':
            d=rotate90left(d)
        elif i=='R':
            d=rotate90right(d)
        else:
            x,y=moveingrid(x,y,d)
        n+=1
    if not flag:
        print(x," ",y," ",d)
    else:
        print("Upper Bound Reached")
        
