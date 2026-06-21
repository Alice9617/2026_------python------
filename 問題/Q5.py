#じゃんけんを行うプログラムをand,orを用いて作成。行数制限10行
print("1がパー,2がグー,3がチョキです。数字で入力してください")
while True:
    a=int(input("A="))
    b=int(input("B="))
    if (a==1 and b==2) or (a==2 and b==3) or (a==3 and b==1):
        print("Aの勝ち")
    elif a==b:
        print("あいこ")
    else:
        print("Bの勝ち")
        