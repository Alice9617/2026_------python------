#1:listの作成
mylist=[]   
mylist2=list() #pythonでのlistは変数=[]の形式で生成できる

#2:listに引数を格納する
mylist=[1,2,3,4]      
print(mylist)         #mylistというリストを宣言してint型の要素（点）を追加

mylist2=["Hello",1,"world",2,"!"]
print(mylist2)                     #また、このようにリスト内にint型以外にも文字列型等のリストを格納可能

#3:appendメソッドで点を追加
mylist=[1,2,3,4]
mylist.append(5)
print(mylist)                     #.appendでリストに新たな点を追加する事ができる

#4:removeメソッドで点を削除
mylist=[1,2,3,4,5]
mylist.remove(5)
print(mylist)                    #.removeでリスト内から指定した点を削除。もし存在しない点を指定するとエラーになる

#5:in演算子で点を検索
mylist=[1,2,3,4,5]
print(3 in mylist)
print("hello" in mylist)         #inでは指定したリスト内に指定した点が入っているかを確認する。入っているならTrue,入っていないならFalseが返ってくる

#6:len関数で点の数をカウント
length=len(mylist)               #len(リスト名)でリスト内に含まれる点の総数を表示する
print(length)


#リストの応用

#ex1:listの内包表記
old=[1,2,3,4,"hello","world"]   
new=[i*2 for i in old]          #list内にある点をiとしてそれをすべて2倍している。なお、文字列型だと同じ文字が二回繰り返される
print(new)

#ex2:joinメソッドで文字列を作成
mylist=["1","2","3","4","hello","world"]
str1=''.join(mylist)
str2=' '.join(mylist)                      #シングルクォーテーションの中に文字を入れることでリスト内の点表示時に間に何を入れるかを指定できる
print(str1)
print(str2)



