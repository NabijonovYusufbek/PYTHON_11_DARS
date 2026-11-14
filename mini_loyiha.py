import csv
import matplotlib.pyplot as plt

FAYL_NOMI = "kitoblar.csv"

def kitoblarni_korish():
    """Barcha kitoblarni ko'rsatish"""
    with open(FAYL_NOMI, "r") as f:
        reader = csv.DictReader(f)
        print("\n--- Kitoblar ro'yxati ---")
        for row in reader:
            print(f"{row['nom']} | {row['kategoriya']} | {row['muallif']} | {row['oqilgan']} marta")

def kitob_qoshish():
    """Yangi kitob qo'shish va CSV faylni yangilash"""
    nom = input("Kitob nomi: ").strip()
    kategoriya = input("Kategoriyasi: ").strip()
    muallif = input("Muallifi: ").strip()
    oqilgan = input("O'qilgan soni: ").strip()

    with open(FAYL_NOMI, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([nom, kategoriya, muallif, oqilgan])
    print("Kitob muvaffaqiyatli qo'shildi!")

def kitob_qidirish():
    """Nom bo'yicha qidirish"""
    kalit = input("Qidirilayotgan kitob nomi: ").strip().lower()
    with open(FAYL_NOMI, "r") as f:
        reader = csv.DictReader(f)
        topildi = False
        for row in reader:
            if kalit in row['nom'].lower():
                print(f"Topildi: {row['nom']} ({row['kategoriya']}, {row['muallif']}) — {row['oqilgan']} marta")
                topildi = True
        if not topildi:
            print("Bunday kitob topilmadi.")

def kategoriya_filtrlash():
    """Kategoriya bo'yicha filtrlash"""
    kat = input("Kategoriya nomi: ").strip().lower()
    with open(FAYL_NOMI, "r") as f:
        reader = csv.DictReader(f)
        print(f"\n--- {kat.title()} kategoriyasidagi kitoblar ---")
        for row in reader:
            if row['kategoriya'].lower() == kat:
                print(f"- {row['nom']} ({row['muallif']})")

def eng_kop_oqilgan():
    """Eng ko'p o'qilgan kitobni topish"""
    with open(FAYL_NOMI, "r") as f:
        reader = list(csv.DictReader(f))
        if not reader:
            print("Fayl bo'sh.")
            return
        eng_mashhur = max(reader, key=lambda x: int(x['oqilgan']))
        print(f"Eng ko'p o'qilgan kitob:\n{eng_mashhur['nom']} — {eng_mashhur['oqilgan']} marta")

def grafik_chiqarish():
    """Kategoriyalar bo/yicha kitoblar sonini grafik qilish"""
    kategoriyalar = {}
    with open(FAYL_NOMI, "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            kat = row['kategoriya']
            kategoriyalar[kat] = kategoriyalar.get(kat, 0) + 1

    plt.bar(kategoriyalar.keys(), kategoriyalar.values(), color='skyblue', edgecolor='black')
    plt.title("Kategoriyalar bo'yicha kitoblar taqsimoti")
    plt.xlabel("Kategoriyalar")
    plt.ylabel("Kitoblar soni")
    plt.show()

# Asosiy menyu
def asosiy():
    while True:
        print("\n--- Kutubxona menyusi ---")
        print("1. Kitoblarni ko'rish")
        print("2. Kitob qo'shish")
        print("3. Kitob qidirish")
        print("4. Kategoriya bo'yicha filtrlash")
        print("5. Eng ko'p o'qilgan kitob")
        print("6. Grafik chiqarish")
        print("0. Chiqish")
        
        tanlov = input("Tanlov: ").strip()
        
        if tanlov == '1': kitoblarni_korish()
        elif tanlov == '2': kitob_qoshish()
        elif tanlov == '3': kitob_qidirish()
        elif tanlov == '4': kategoriya_filtrlash()
        elif tanlov == '5': eng_kop_oqilgan()
        elif tanlov == '6': grafik_chiqarish()
        elif tanlov == '0': break
        else: print("Noto'g'ri tanlov, qaytadan urinib ko'ring.")

if __name__ == "__main__":
    asosiy()