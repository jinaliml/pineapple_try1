a=800
b=800
while(1):
    player1=input("player 1 입력하세요:")
    if player1.split(",")[0]=="a":
        a-=int(player1.split(",")[1])
    elif player1.split(",")[0]=="b":
        b-=int(player1.split(",")[1])
    if a==0 and b==0: 
        print("player 1 win")
        break
    print(a,b)
    player2=input("player 2 입력하세요:")
    if player2.split(",")[0]=="a":
        a-=int(player2.split(",")[1])
    
    elif player2.split(",")[0]=="b":
        b-=int(player2.split(",")[1])
       
    if a==0 and b==0: 
        print("player 2 win")
        break
    print(a,b)    
