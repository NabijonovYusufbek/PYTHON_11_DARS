matn = "Python dasturlash qiziqarli. Python imkoniyatlari keng."

sozlar = matn.split()
print("So'zlar soni:",len(sozlar))
print("Eng uzun soz:",max(sozlar, key=len))
letters = [char for char in matn.lower() if char.isalpha()]

harflar = matn.replace(" ", "")
eng_kop = max(set(harflar), key=harflar.count)
print("Eng ko'p uchragan harf:", eng_kop)

takrorlanmaydigan = []

for soz in sozlar:
    if sozlar.count(soz) == 1:
        takrorlanmaydigan.append(soz)

print("Takrorlanmaydigan so'zlar:", ", ".join(takrorlanmaydigan))