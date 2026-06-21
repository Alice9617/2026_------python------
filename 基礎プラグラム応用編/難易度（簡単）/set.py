#1:set型
myset1=set([1,2,3])
myset2=set([1,2,3,3,2,1])
print(myset1)
print(myset2)             #set型では重複する要素は無視される

#2:setへの要素の追加
myset=set([1,2,3])
myset.add(4)              #.add(追加したい要素)でsetに要素を追加する
print(myset)            

#3:setからの要素の削除
myset=set([1,2,3])
myset.remove(3)          #.remove(消したい要素)でsetから要素を削除する
print(myset)

myset.clear()
print(myset)             #set内の要素をすべて削除したいときはclear()を用いる

#set型を用いることによる集合の計算

#和集合の計算
A={1,2,3}
B={3,4,5}
C=A|B
print(C)               #集合A|集合Bで和集合ができる。ちなみに|は日本語で「パイプ」

C=A.union(B)
print(C)              #集合A.union(集合B)でも和集合を作れる

#積集合の計算
A={1,2,3}
B={3,4,5}
C=A&B
print(C)              #集合A&集合Bで積集合を求められる

C=A.intersection(B)
print(C)              #集合A.intersection(集合B)でも積集合を作れる

#差集合
A={1,2,3}
B={3,4,5}
C=A-B
print(C)              #集合Aー集合Bで差集合を作れる

C=A.difference(B)
print(C)              #集合A.difference(B)で差集合を作れる

#排他的論理和集合
A={1,2,3}
B={3,4,5}
C=A^B
print(C)              #集合A^集合Bで排他的論理和（全体から積集合を引いたもの）集合を求められる

C=A.symmetric_difference(B)
print(C)                      #集合A.symmetric_difference(集合B)でも排他的論理和集合を求められる

#ALT編

#list型からset型を作る方法
mylist=[11,1,3,5,3,6,7,8,9,23,23,5]
myset=set(mylist)                    #list型をset型に直すには単純にリストをset()でセット化すればよい
print(myset)




