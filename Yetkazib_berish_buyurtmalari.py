buyurtmalar = [
 {"mahsulot": "Kitob", "narx": 45000, "miqdor": 2},
 {"mahsulot": "Ruchka", "narx": 5000, "miqdor": 10},
 {"mahsulot": "Sumka", "narx": 180000, "miqdor": 1}
]

for i in buyurtmalar:
    print(f"{i["mahsulot"]}: {i["narx"] * i["miqdor"]}")

eng_qimmat = max(buyurtmalar, key=lambda x: x["narx"] * x["miqdor"])
umumiy_narx = eng_qimmat["narx"] * eng_qimmat["miqdor"]
print(f"Eng qimmat mahsulot: {eng_qimmat["mahsulot"]}--> {umumiy_narx} so'm")
