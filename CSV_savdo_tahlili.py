import csv

tushumlar = {}
with open("11_Dars/savdo.csv","r") as f:
    data = csv.DictReader(f)
    malumotlar = list(data)
    for qator in malumotlar:
        kat = qator["kategoriya"]
        summa = int(qator["narx"]) * int(qator["miqdor"])
        tushumlar[kat] = tushumlar.get(kat, 0) + summa

for kat, summa in tushumlar.items():
    print(f"{kat}: {summa:,} so'm")

eng_yaxshi = max(tushumlar, key=tushumlar.get)
print(f"Eng daromadli kategoriya: {eng_yaxshi}")

    