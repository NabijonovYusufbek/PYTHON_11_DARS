natijalar = [
 {"ism": "Aziza", "ball": 82},
 {"ism": "Jasur", "ball": 64},
 {"ism": "Madina", "ball": 91},
 {"ism": "Sardor", "ball": 70}
]

Yuqori_ballar = list(filter(lambda ball: ball["ball"] >= 70,natijalar))
ismlar = list(map(lambda x: x["ism"],Yuqori_ballar))
print("70 dan yuqori ball olganlar:",*ismlar)

oshirilgan_ball = list(map(lambda x: x["ball"] + ((x["ball"] * 10) / 100),natijalar))
print("10 % ga oshirildi:",oshirilgan_ball)