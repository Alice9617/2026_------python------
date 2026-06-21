#range文を使用した九九表表示プログラム
for i in range (1,10):
    for j in range(1,10):
        print(f"{i*j:3}", end="")       #:数字で結果を何桁で表示するか指定できる。今回は３桁。end=""は改行する意味を示す
    print()





