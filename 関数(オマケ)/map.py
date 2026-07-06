#基本構文
def add_suffix(animal):
    return "動物："+animal
animals =["イヌ","ネコ","ウサギ"]
result=list(map(add_suffix,animals)) #list(map(入れたい処理))で適用
print(result)

#まとめて処理を適用する(例:文字の大文字化)
animals=["lion","tiger","panda","giraffe"]
uppercase_animals=list(map(str.upper,animals)) #str.upper関数をmap関数で全引数に適用している
print(uppercase_animals)

#数値リストの計算処理
dog_ages=[1,2,3,4,5,]
human_ages=list(map(lambda age:age*7,dog_ages)) #リスト内の全ての数字に処理を適用している
print(f"イヌの年齢:{dog_ages}")
print(f"人間換算年齢:{human_ages}")

#文字列から整数への型変換
animal_counts=["12","8","15","3","20"]
count_numbers=list(map(int,animal_counts))  #map関数を利用することでintをリスト内の全ての文字列に適用している
total_animals=sum(count_numbers)
print(f"各動物数:{count_numbers}")
print(f"総数:{total_animals}匹")

#複数リストの同時処理
animals=["イヌ","ネコ"]
sounds=["ワン","ニャー"]
animal_sounds=list(map(lambda a,s:f"{a}は{s}と鳴きます",animals,sounds)) 
#map関数は複数のリストを引数として受け取れる
for sound in animal_sounds:
    print(sound)

#条件付き文字列操作処理
animals=["NYANCAT"]
short_names=list(map(lambda name:name[:2]+"..."
                     if len(name)>3           #lambda関数を用いて動物の名前の文字数に応じて処理を変更している。
                     else name,animals))
print("元の名前:",animals)
print("短縮名:",short_names)

#データの正規化処理
import math
weights=[12.7,45.2,8.9,23.1,67.8]         #浮動小数点数のリストに対して四捨五入の処理を行っている。
rounded_weights=list(map(lambda w:round(w),weights))
print("元の体重:",weights)
print("四捨五入後:",rounded_weights,"kg")

#辞書データの値抽出処理
animals_data=[
    {"name":"ライオン","age":5},
    {"name":"ゾウ","age":15}
]
#lambda関数を利用してリスト内のある特定のキーのみにアクセスしている
names=list(map(lambda animal:animal["name"],animals_data))

#ネストしたリスト構造の処理
zoo_areas=[
    ["ライオン","トラ","ヒョウ"],
    ["ゾウ","キリン"],
    ["サル","チンパンジー","オランウータン","ゴリラ"]
]
#入れ子になったリスト構造に対してlen関数を適用し、それぞれのリストの要素数を取得している
area_counts=list(map(len,zoo_areas))        
print("各エリアの動物数:",area_counts)
print("総動物数",sum(area_counts))
