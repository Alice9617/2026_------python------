#基本構文
add_lambda=lambda x,y:x+y   #基本的な書き方は[lambda引数:戻り値]
print(add_lambda(3,5))      #通常の関数定義よりより軽量に済ませらられる

#リストの各要素を変換する処理
animals=["cat","dog","rabbit","hamster"]
uppercase_animals=list(map(lambda x:x.upper(),animals)) 
#mapの全ての要素に処理を行う性質を利用して値の一斉計算ができる
print(uppercase_animals)

#条件に合う要素を抽出する処理
animals=["ネコ","イヌ","ウサギ","ハムスター","カメ"]
long_name_animals=list(filter(lambda x:len(x)>=3,animals))
print(long_name_animals)

#数値リストの並べ替え処理
animals_weights=[("ネコ",4.5),
                 ("イヌ",12.3),
                 ("ウサギ",2.1),
                 ("ハムスター",0.15)]
sorted_animals=sorted(animals_weights,key=lambda x:x[1]) 
#sorted関数用いることで指定したkeyの値をソートできる
print(sorted_animals)

#辞書データの並び替え処理
animals_data=[{"name":"ネコ","age":3},
              {"name":"イヌ","age":7}]
#本コードではわかりにくいが数値の並び替え処理もできる
sorted_by_age=sorted(animals_data,key=lambda x:x["age"]) 
print(sorted_by_age)

#数値演算の一括処理
weights=[4.5,12.3,2.1,0.15]
doubled_weights=list(map(lambda x:x*2,weights))
print(doubled_weights)

#文字列の部分抽出処理
animals=["ネコ","イヌ","ウサギ","ハムスター","カメ"]
first_chars=list(map(lambda x:x[0],animals))  #文字列の先頭だけをkeyのvalueとして引き出している    
print(first_chars)

#複合条件でのフィルタリング処理
animals=[("ネコ",4.5,3),
         ("イヌ",12.3,7)]
#key[1]にしていした条件とkey[2]にしていした条件を満たすものだけを表示している
filtered=list(filter(lambda x:x[1]>=5 and x[2]<5 ,animals)) 
print(filtered)

#最小値、最大値の検索処理
animals=[("ネコ",4.5),
         ("イヌ",12.3)]
lightest_animal=min(animals,key=lambda x:x[1]) #key[1]の値の最小値をmin関数で探索している
print(lightest_animal)

