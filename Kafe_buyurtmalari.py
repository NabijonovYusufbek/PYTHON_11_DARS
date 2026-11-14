menu = {"lavash": 28000, "somsa": 10000, "choy": 5000}

def buyurtma(*args, **kwargs):
    print("--- MIJOZ MA'LUMOTLARI ---")
    for kalit, qiymat in kwargs.items():
        print(f"{kalit.capitalize()}: {qiymat}")
    
    print("\n--- BUYURTMA ---")
    jami = 0
    
    for mahsulot in args:
        if mahsulot in menu:
            narx = menu[mahsulot]
            jami += narx
            print(f"- {mahsulot}: {narx} so'm")
        else:
            print(f"- Ogohlantirish: '{mahsulot}' menyuda yo'q!")
            
    print(f"\nJami summa: {jami} so'm")
ism = input("Mijoz ismi: ")
raqam = int(input("Telefon raqam: "))
buyurtma("lavash", "choy", "somsa", mijoz=ism, telefon=raqam)