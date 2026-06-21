#入力した結果の大小関係をifで調べ、結果を表示するプログラムの作成。行数制限10行
a=int(input("A="))
b=int(input("B="))
if a<b:
    print("Bの方が大きいです")
elif b<a:
    print("Aの方が大きいです")
else:
    print("AとBは等しいです")
