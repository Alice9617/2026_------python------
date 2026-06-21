#whileループで和差積商を計算し続けるプログラムを作成。 行数制限15行
while True:
    mode=int(input("1が加法、2が減法、3が積、4が商です"/"モードを入力"))
    a=int(input("a="))
    b=int(input("b="))
    if mode==1:
        print(a+b)
    elif mode==2:
        print(a-b)
    elif mode==3:
        print(a*b)
    elif mode==4:
        print(a/b)
    else:
        print("他のモードを入力しないでください")
        
    
