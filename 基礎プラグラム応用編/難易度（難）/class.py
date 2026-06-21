#1:classについて
class Animals:
    def __init__(self,name): 
        self.name = name                               
    def speak(self):
        return f"{self.name}が鳴きました"

dog = Animals("イヌ")
print(dog.speak())
#上記のコードではAnimalというclassを定義した後、nameというインスタンス（classが設計図ならインスタンスは設計図を基に作られたもの）変数と
#speakというメソッド（処理をまとめたもの。関数。）を持たせている。
#よって、dog変数にはAnimalクラスのインスタンスを作成して代入し、そのインスタンスの関数を呼び出している。


#2:基本的なclassの作成
class Animal:
    def __init__(self,name,species):
        self.name,self.spicies = name,species

dog = Animal("ポチ","イヌ")                #classでは関連するデータについて一つの単位としてまとめることで基本情報を保持することが可能
print(f"{dog.name}は{dog.spicies}です")

#3:メソッドの追加
class Animals:
    def __init__(self,name,sound):
        self.name,self.sound = name,sound
    def speak(self):
        return f"{self.name}が{self.sound}と鳴きました"

print(Animals("イヌ","ワン").speak())

#classはデータと操作を一緒に定義できる点でもある。上記のコードではAnimalsクラスに鳴き声メソッドを追加している
#self引数を使って自分自身のデータにアクセスする方法を示している。selfはインスタンス自信を示すものとなっている

#4:コンストラクタの活用
class Animals:
    def __init__(self,name,species="不明",age=0):
        self.name,self.species,self.age = name,species,max(0,age)
    def info(self):
        return f"{self.name}({self.species}){self.age}歳"

print(Animals("ポチ","イヌ",3).info())
#インスタンス作成時に初期設定を行いたい場合はコンストラクタを用いる。以上のコードでは、デフォルト値や値の検証も含めた初期化
#オブジェクト生成時のデータ整合性を確保するために用いられる

#5:クラス変数とインスタンス変数
class Animals:
    count = 0
    def __init__(self,name):
        self.name = name; Animals.count += 1
    def info(self):
        return f"{self.name}(全{Animals.count}匹中)"

Animals("イヌ"),Animals("ネコ")
print(Animals("ウサギ").info())
#クラス変数とインスタンス変数の違いを表したコード。すべてに作用するクラス変数と自分のみに作用するインスタンス変数の違いが示されている

#6:継承の基本
class Animal:
    def __init__(self,name):
        self.name=name
    def speak(self):
        return f"{self.name}が鳴きました"
class Dog(Animal):
    def fetch(self):
        return f"{self.name}がボールを取ってきました"
print(Dog("イヌ").speak())
#親クラスの機能を再利用品がら継承する方法を示したもの。既存クラスの特性を引き継げる

#7:メソッド(関数)のオーバーライド
class Animal:
    def __init__(self,name):
        self.name =name
    def speak(self):
        return f"{self.name}が鳴きました"
class Cat(Animal):
    def speak(self):
        return f"{self.name}がニャーと鳴きました"
print(Cat("ネコ").speak())
#継承したclassでは親クラスで定義された関数の再定義が可能。以上のコードは同じインタフェースを保ちながら動作を変更する多態性の原則を示している

#8:特殊メソッド（マジックメソッド）
class Animal:
    def __init__(self, name, species): self.name, self.species = name, species
    def __str__(self): return f"{self.species}の{self.name}"
    def __eq__(self, other): return self.species == other.species

print(Animal("ポチ", "イヌ"), Animal("ポチ", "イヌ") == Animal("タロウ", "イヌ"))
#特殊メソッド（__init__のような特殊な関数）をカスタマイズすると、クラスの動作が制御可能になる

#9:プロパティの活用
class Animal:
    def __init__(self,name):
        self.name = name; self.age = 0
        @property
        def age(self):
            return self._age
        @age.setter
        def age(self,value):
            self._age =max(0,value)

dog = Animal("イヌ"); dog.age =3; print(f"{dog.name}は{dog.age}歳")
#プロパティ（@~）を用いると、関数を属性のように扱える。データの整合性を保ちながらシンプルなインタフェースが提供できる

