#1:辞書の作成
empty_dict = {}   #作りたい辞書名={}で空の辞書を作成
print(empty_dict)

#2:辞書の更新・削除
animal_dict = {"cat":"myaou"}
print(animal_dict)
animal_dict["ウシ"]="モー"              #辞書名["追加したいキー"]="追加したい要素"で新たにkeyを辞書に追加する
print(animal_dict)

zoo_dict={"cat":1,"rion":2,"dog":3}
print("更新前",zoo_dict)

del zoo_dict["dog"]                    #del 辞書名[キー]で辞書から指定した項目を削除する
print("更新後：",zoo_dict)

#3:辞書のキーと値の取得
human_sounds={"（笑）":"www","冷笑":"うおw"}
print("キー一覧：",list(human_sounds.keys()))      #.keys()で辞書内からキーの一覧を取得
print("値一覧：",list(human_sounds.values()))      #.values()で辞書の値の一覧を取得
print("j民の鳴き声",human_sounds.get("j民","不明")) #.get()で存在しないキーでもエラーにならずに指定した値を返す

#4:辞書同士の結合・コピー
animals_dict=human_sounds.copy()                 #.copyで指定した辞書の内容をコピー
animals_dict.update(zoo_dict)                    #.updateで辞書に指定した辞書の内容を追加
print("結合結果",animals_dict)

#5:条件分岐での辞書活用
animal_actions={"cat":"毛づくろい","dog":"散歩"}
animal="cat"
if animal in animal_actions:                            #in演算子でkeyが辞書に含まれているかを確認。含まれていたらvalueの内容を表示
    print(f"{animal}は{animal_actions[animal]}をします") 
else:
    print("不明な生物を検出しました")

#6:ループ処理での辞書操作
animal_colors={"cat":"白色","dog":"茶色"}     
for animal, color in animal_colors.items():    #.items()でkeyとvalueのペアを取得　この場合、animalがkeyを指定し、colorがvalueを示す
    print(f"{animal}の色は{color}です")         #この文章で取得した情報を繰り返し辞書の終わりまで表示

#7:ネストした辞書の操作
animals_info={
    "raion":{"生息地":"アフリカ","体重":"190kg"},          #このように辞書の中に辞書を組み込むことができる
    "pengin":{"生息地":"南極","体重":"3kg"}
} 
print("ライオンの生息地",animals_info["raion"]["生息地"])  #また、辞書の内容を指定して引き出すことができる
print("ペンギンの生息地",animals_info["pengin"]["体重"]) 

#8:辞書内包表記
animals={"cat","dog","rabbit"}
animal_lengths={animal: len(animal) for animal in animals} #animalsリストから要素を一つずつ取り出し、取り出した要素をanimalという変数に入れる
print("動物名の文字数:",animal_lengths)                     #これを辞書内包表記といい、{キー: 値 for 変数 in リスト}の形で扱う
#処理的には、animalsからキーを取得し、animalという変数に入れた後、animalをキーとした辞書を作成する。valueはlen()で各キーの文字数を抽出したものにしている。
