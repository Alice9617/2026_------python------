def A(x,y,a):
    if a==1:
        result=x+y
    elif a==2:
        result=x-y
    elif a==3:
        result=x*y
    elif a==4:
        result=x/y
    else :
        print("1~4以外の数字を入力しないでください")
        return None
    return result

while True:
    print("モードを入力。１は加算。２は減算。３は乗算。４は除算です。")
    a=int(input("モードを入力："))
    x=int(input("x:"))
    y=int(input("y:"))
    print (A(x,y,a))