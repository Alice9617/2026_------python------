while True:
    print("モードを選んでください" \
    "1なら加法" \
    "2なら減法です")
    a=int(input("モード="))
    if a==1:
        print("加法モードが選択されました。計算したい数字を入力してください")
        b=float(input("a="))
        c=float(input("b="))
        print(b+c)
    elif a==2:
        print("減法が選択されました。計算したい数字を入力してください")
        d=float(input("a="))
        e=float(input("b="))
        print(d-e)
    else:
        print("無効な数字又は文字が入力されました。再度入力してください")
        
        

