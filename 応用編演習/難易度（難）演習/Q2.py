class Apalel:
    def __init__(self,id,name,price,purchase_price):
        self.id=id
        self.name=name
        self.price=price
        self.purchase=purchase_price

    def messod(self):
        Genka=(self.purchase/self.price)
        return Genka


coolT= Apalel("A0001","半袖クールTシャツ",5000,2250)
Genka=coolT.messod()
print(Genka)

coolT.price=6000 
Genka=coolT.messod()       #再計算を忘れずに！
print(Genka)



