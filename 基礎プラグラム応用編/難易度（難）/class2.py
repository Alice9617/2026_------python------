#美容室を予約するアプリを作成する（詳しくはhttps://www.youtube.com/watch?v=tCMl1AWfhQQ）の1::55:00あたりを参照
#オブジェクトを共通する属性でまとめたものをクラスという
#インスタンス変数はクラスが持つ属性

#クラスが持つ処理をメソッドという。関数で定義される

#美容院オブジェクト




#ユーザーオブジェクト
class User:
    #インスタンス変数の初期化(イニシャライザ)
    def __init__(self,name,mail_address,point): #メソッドの第一引数は慣習としてselfを用いる
        self.name =name                         #
        self.mail_address =mail_address
        self.point=point 

    def add_point(self,point):
        self.point +=point

    

user_1=User("佐藤葵","sato@example.com",500) #()内はそれぞれname,mail_address_point.
user_2=User("小林ゆい","kobayashi@example.com",1000)
x=user_1.name
y=user_2.name

print(user_1.point)
print(user_2.point)

#書き換え処理
user_1.add_point(100)
user_2.add_point(100)
print(user_1.point)
print(user_2.point)
