import math 

shaharlar = {
    "A": (0, 0), 
    "B": (3, 4), 
    "C": (6, 0)
}

def masofa_hisobla(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

nomlar = list(shaharlar.keys())  

eng_katta_masofa = 0
eng_uzoq_juftlik = ("", "")

print("--- Barcha shaharlar orasidagi masofalar ---")

for i in range(len(nomlar)):
    for j in range(i + 1, len(nomlar)):
        sh1 = nomlar[i]  
        sh2 = nomlar[j] 
        
        d = masofa_hisobla(shaharlar[sh1], shaharlar[sh2])
        
        print(f"{sh1} va {sh2} orasidagi masofa: {d}")
        
        if d > eng_katta_masofa:
            eng_katta_masofa = d
            eng_uzoq_juftlik = (sh1, sh2)

print("----------------------------------------")
print(f"Eng uzoq juftlik: {eng_uzoq_juftlik[0]} va {eng_uzoq_juftlik[1]} shaharlari")
print(f"Ular orasidagi eng katta masofa: {eng_katta_masofa}")