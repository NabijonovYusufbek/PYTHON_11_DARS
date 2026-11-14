import json

with open("11_Dars/sozlamalar.json","r") as f:
    data = json.load(f)
    print(data)

Mavzu = input("Mavzu light/dark: ")
bildirishnoma = input("Bildirishnoma True/False: ")
data["mavzu"] = Mavzu
data["bildirishnoma"] = bildirishnoma

with open("11_Dars/sozlamalar.json","w") as f:
    json.dump(data,f,indent=4)
    print("----Malumot Yangilandi------")
    print(data)
