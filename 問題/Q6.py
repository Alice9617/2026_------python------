#defで関数を作り和差積商を計算　行数制限20行
def A(x,y,a):
    if a==1:
        result=x+y
    elif a==2:
        result=x-y
    elif a==3:
        result=x*y
    elif a==4:
        result=x/y
    return result

while True:
    print("モードを入力。１は加算。２は減算。３は乗算。４は除算です。")
    a=int(input("モードを入力："))
    if a>=5:
        print("想定外のモードが入力されました。再入力してください")
        continue
    x=int(input("x:"))
    y=int(input("y:"))
    print (A(x,y,a))