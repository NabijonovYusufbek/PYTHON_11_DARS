# def xavfsiz_bolish(son1, son2):
#   try:
#     a = float(son1)
#     b = float(son2)

#     assert b != 0, "Assert xatoligi: 2 chi son nol bo'lishi mumkin emas!"
    
#     natija = a / b
#     return natija

#   except ValueError:
#     return "Xatolik: Son o'rniga matn yoki yaroqsiz belgi kiritildi!"
#   except ZeroDivisionError:
#     return "Xatolik: Sonni nolga bo'lib bo'lmaydi!"
#   except AssertionError as e:
#     return str(e)


# def bolish(a, b):
#     assert a.isdigit() and b.isdigit(),"Son kiritish kerak"
    
#     assert int(b)!=0,"B son 0ga teng bo'lmasligi kerak"
    
#     return int(a) / int(b)

# son1 = input("Birinchi son: ")
# son2 = input("Ikkinchi son: ")
# try:
#     natija = bolish(son1, son2)
#     print("Natija:", natija)
# except Exception as e:
#     print(e)


def bolish(a, b):
    
    if not(a.isdigit() and b.isdigit()):
        raise ValueError("Son kiriting!")
    
    if int(b) == 0:
        raise ZeroDivisionError("B son 0ga teng bo'lmasligi kerak")
    
    return int(a) / int(b)

son1 = input("Birinchi son: ")
son2 = input("Ikkinchi son: ")
try:
    natija = bolish(son1, son2)
    print("Natija:", natija)
except Exception as e:
    print(e)

son = input("Son= ")
son1 = input("Son= ")
print(bolish(son,son1))  
 