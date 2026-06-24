customer1=set(["田中","佐藤","鈴木","中村"])
customer2=set(["鈴木","佐藤","斉藤","坂田"])

#顧客数（１）
print(f"C1顧客人数:{len(customer1)}")

#顧客数（２）
print(f"C2顧客人数:{len(customer2)}")

#どちらか一方に所属している(A)
ONLY_A=customer1-customer2
print(f"C1のみに所属：{ONLY_A}")

#どちらか一方に所属している
ONLY_B=customer2-customer1
print(f"C2のみに所属:{ONLY_B}")

#どちらか一方でも所属している
BOTH=customer1.union(customer2)
print(f"どちらか一方に所属:{BOTH}")

#会員登録システム

