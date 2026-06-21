print("1がパー,2がグー,3がチョキです。数字で入力してください")
while True:
    a=int(input("A="))
    b=int(input("B="))
    if a==1 and b==2:
        print("Aの勝ち")
    elif a==2 and b==3:
        print("Aの勝ち")
    elif a==3 and b==1:
        print("Aの勝ち")
    elif a==b:
        print("あいこ")
    else:
        print("Bの勝ち")
        