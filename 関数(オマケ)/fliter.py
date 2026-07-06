#基本構文
def is_positive(num):
    return num>0

values=[-3,-1,0,2,5,-8]
#filter(関数,繰り返し取り出せるオブオブジェクト）
positive_values=list(filter(is_positive,values)) 
print(positive_values)

#文字列長による動物名フィルタリング
animals=['イヌ','ネコ','ゾウ','キリン','カバ']
long_names=list(filter(lambda name:len(name)>=3 ,animals))
print(long_names)

#数値範囲による動物の体重フィルタリング
animal_weights=[('イヌ',15),
                ('ゾウ',5000),
                ('ネコ',4)]
heavy_animals=list(filter(lambda x:x[1]>100 ,animal_weights))
print(heavy_animals)

#特定文字を含む動物名の抽出
zoo_animals=["ライオン","トラ","ヒョウ"]
#特定文字を所持するリスト内のデータをlambdaを用いて検索している
animals_with_vowel=list(filter(lambda name:"ウ" in name ,zoo_animals))
print(animals_with_vowel)

#辞書データから条件に合う動物情報の抽出
animals_data=[
    {"name":"パンダ","type":"哺乳類","endangered":True},
    {"name":"イルカ","type":"哺乳類","endangered":False}
]
#key[endangered]にあるvalueのTorFを引き出している
endangered =list(filter(lambda x:x["endangered"],animals_data))
print(endangered)

#None値を除外した動物リストの作成
mixed_animals=["ウサギ",None,"リス","","ハムスター",None]
clean_animals=list(filter(None,mixed_animals)) #Noneを持つものを自動的に除外している
print(clean_animals)

#複数条件による動物データの絞り込み
pets=[("ハムスター",1),
      ("ウサギ",3),
      ("インコ",5)]
young_pets=list(filter(lambda pet:pet[1]<4 and "ウサギ" in pet[0],pets))
print(young_pets)

#偶数インデックスの動物名抽出
safari_animals=["ライオン","シマウマ","サイ","カバ"]
#enumerate関数と組み合わせることでデータの位置情報を活用した抽出処理が実現できる
even_index_animals=list(filter(lambda x:x[0]%2==0 ,enumerate(safari_animals)))
result=[animal for index, animal in even_index_animals]
print(result)
