def A(x,y,mode):
    if mode==1:
        result=x+y
    elif mode==2:
        result=x-y
    else:
        print("これ以外のモードを入力しないでください！")
        return None
    return result

print("モードを選択。１：加法,２：減法")
mode=int(input("モード＝"))
print("任意の数字を入力してください")
x=int(input("a="))
y=int(input("b="))
print(A(x,y,mode))