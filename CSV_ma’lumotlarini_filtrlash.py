import csv

yonalish = input("Yo'nalish: ").strip()

with open("talabalar.csv", "r") as f:
    reader = csv.DictReader(f)
    saralangan = [row for row in reader if row["yonalish"].lower() == yonalish.lower()]

saralangan.sort(key=lambda x: int(x["ball"]), reverse=True)

with open("filtrlangan_talabalar.csv", "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=["ism", "yosh", "yonalish", "ball"])
    writer.writeheader()
    writer.writerows(saralangan)

print(f"{len(saralangan)} ta talaba topildi.")
print("Natijalar filtrlangan_talabalar.csv fayliga yozildi.")