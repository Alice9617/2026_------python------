#1:for文
mylist=["i"]
for q in mylist:           #forの後に新たな変数を生成してオブジェクトと結び付け、そのあとに処理を実行する
    print(q)

#2:range関数基本編
for num in range(10):      #同処理を何度も繰り返したい場合はrange関数を用いる
    print(f"結果1：{num}")

for sum in range(3,10):   #range関数の()の中身は基本、（start,stop）という仕組みになっている。
    print(f"結果2：{sum}")

#3:range関数基礎
for hum in range(3,10,2):  #range関数の()の変数が3つの時は、(開始点、終点、増加量)となっている
    print(f"結果３：{hum}")

#4:brakeによるプログラムの終了
for mum in range(20):
    print(f"結果４:{num}")
    if num == 10:
        break              #for文では処理にbreakを用いることで処理を終了させることができる

#5:continueによる処理続行
for cum in range(2,10):
    if cum % 2==0:
        print("偶数",cum)
        continue           #for文ではcontinueでifを用いても処理を続行させることができる
    else:
        print("奇数",cum)

foods=["apple","beef","chocolate"]
for food in reversed(foods):       #reversed(配列)を用いると配列の要素が逆順に取得できる
    print(food)                   
    


