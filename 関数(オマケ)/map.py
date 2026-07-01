def add_suffix(animal):
    return "動物："+animal
animals =["イヌ","ネコ","ウサギ"]
result=list(map(add_suffix,animals))
print(result)

#まとめて処理を適用する(例:文字の大文字化)
animals=["lion","tiger","panda","giraffe"]
uppercase_animals=list(map(str.upper,animals))
print(uppercase_animals)

#数値リストの計算処理
dog_ages=[1,2,3,4,5,]
human_ages=list(map(lambda age:age*7,dog_ages))
print(f"イヌの年齢:{dog_ages}")
print(f"人間換算年齢:{human_ages}")

#文字列から整数への型変換
animal_counts=["12","8","15","3","20"]
count_numbers=list(map(int,animal_counts))
total_animals=sum(count_numbers)
print(f"各動物数:{count_numbers}")
print(f"総数:{total_animals}匹")

#複数リストの同時処理
animals=["イヌ","ネコ"]
sounds=["ワン","ニャー"]
animal_sounds=list(map(lambda a,s:f"{a}は{s}と鳴きます",animals,sounds))
for sound in animal_sounds:
    print(sound)

#条件付き文字列操作処理
animals=["NYANCAT"]
short_names=list(map(lambda name:name[:2]+"..."
                     if len(name)>3 
                     else name,animals))
print("元の名前:",animals)
print("短縮名:",short_names)

#データの正規化処理
import math 
weights=[12.7,45.2,8.9,23.1,67.8]
rounded_weights=list(map(lambda w:round(w),weights))
print("元の体重:",weights)
print("四捨五入後:",rounded_weights,"kg")

#辞書データの値抽出処理
animals_data=[
    {"name":"ライオン","age":5},
    {"name":"ゾウ,"age:15}
]
names=list(map(lambda animal:animal["name"],animals_data))