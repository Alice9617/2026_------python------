#成績評価システム　解答例1
result=[
    {"ID":"A001",
    "name":"田中",
    "purchases":{
        "japanese":85,
        "math":65,
        "english":73
        }
    },
    {"ID":"A002",
     "name":"佐藤",
     "purchases":{
         "japanese":72,
         "math":55,
         "english":93
        }
    },
]

for key in result:
    scores= key["purchases"]
    japanese=scores["japanese"]
    math=scores["math"]
    english=scores["english"]
    avg=(japanese+math+english)/3
    print(key["name"],":",avg)


