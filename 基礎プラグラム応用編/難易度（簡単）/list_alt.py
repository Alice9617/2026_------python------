#1:extend
mylist=[1,2,3,4,5,6,7,8,9,10]
mylist.extend([11])          #.extendでリスト自体を拡張する。appendはリストに点を増やす。複数追加できるのが強み
print(mylist)

#2:insert
mylist.insert(2,4)          #.insert(何番目,挿入したい要素)で指定した場所に点を追加することができる
print(mylist)

#3:pop
mylist2=[1,2,3,4,5]
mylist2.pop(2)             #.pop(何番目)でその点の次の点を削除する
print(mylist2)

#4:clear
mylist3=[1,2,3]
mylist3.clear()           #.clear()でリスト内の全ての点を削除する
print(mylist3)

#5:count
mylist4=[1,2,3,4,5]
print(mylist4.count(2))  #.countでリスト内に指定した点が何個あるかを数字で表示する

#.sort
mylist5=[1,3,78,56,23,44,31]
mylist5.sort()               #.sort()でリスト内の点を左から小さい順に整理する
print(mylist5)

#copy
mylist6=["hello"]
mylist5=mylist6.copy()
print(mylist5)

