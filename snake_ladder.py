from random import randint
print("-------------------------Welcome to Snake and Ladder!!!----------------------\n\n")
nump=int(input("Number of players"))
pla=[]
initial=[]
for i in range(1,nump+1):
    a=input("Name of player {} ".format(i))
    pla.append(a)
    initial.append(1)
ladder={}
ladder[4]=14
ladder[9]=31
ladder[21]=42
snake={}
snake[17]=7
snake[54]=34
snake[87]=36
b=True
final=[]
print("Let's Play!!\n\n")
turn=0
fin=0
cu=1
while(b):
    print(pla[turn]," throws die, position is ",initial[turn])
    x=randint(1,6)
    print("Number on die is ",x)
    initial[turn]+=x
    if initial[turn] in ladder.keys():
        print("+++++++Yesss!!++++++++")
        initial[turn]=ladder[initial[turn]]
    if initial[turn] in snake.keys():
        print("=======Noooo!!========")
        initial[turn]=snake[initial[turn]]
    if initial[turn]>100:
        need=100-initial[turn]+x
        initial[turn]-=x
        print("You need ",need," to win the game\n")
    elif initial[turn]==100:
        print("#####",pla[turn]," has won the game","#####\n\n")
        temp=[]
        temp.append(pla[turn])
        temp.append(initial[turn])
        final.append(temp)
        count=0
        for i in initial:
            if i!=100:
                count+=1
                break
        if count==1:
            temp.append(pla[turn])
            temp.append(initial[turn])
            final.append(temp)
        if count==0 or count==1:
            print("Game Finished")
            fin=1
            break
    print(pla[turn],"'s new location is ",initial[turn]," \n")
    turn+=1
    if turn==nump:
        print("-----------Round ", cu," finished------------ \n\n")
        cu+=1
        turn=0
    if initial[turn]==100:
        turn+=1
    print("Next turn is of ",pla[turn],"\n\n")
    comand=int(input("1.play 2.stop 3.Positions 4.setting\n\n"))
    if comand==2:
        print("Good Bye!!")
        break
    elif comand==3:
        print("Score\t Name")
        for i in range(0,nump):
            print(initial[i],"   \t",pla[i])
        print("\n\n")
        inpu=int(input("1.play 2.stop"))
        if inpu==2:
            print("Good Bye!!")
            break
    elif comand==4:
        inp=int(input("1.Remove Player 2.Add Player 3.Restart\n\n"))
        if inp==1:
            name=input("Name of player to remove")
            k=0
            fla=0
            for i in pla:
                if i==inp:
                    fla=-1
                k+=1
            if fla==-1:
                pla.remove(inp)
                del initial[k]
                nump-=1
                print(inp," is removed\n\n")
            else:
                print("Player not found\n\n")
        elif inp==2:
            name=input("Name of New player")
            pla.append(name)
            initial.append(1)
            nump+=1
        elif inp==3:
            for i in range(0,nump):
                initial[i]=1
            print("Game restarted!!\n\n")
if fin==-1:
    for i in final:
        for j in i:
            print(j,end="\t")
else:
    print("Score\t Name")
    for i in range(0,nump):
        print(initial[i],"   \t",pla[i])
