#Este exercicio calcula o ano bissexto a partir do periodo greforian
#o objetivo e usar os comando aprendidos sendo eles input,if,elif,else
#tambem o uso do "%" que permite trabalahr com o resto da divisao e "!=" que #permite comparar

year = int(input("Enter a year: "))
if year < 1582:
    print("Not  within the Gregorian calendar period")
else:
    if year % 4 != 0 :
        print("common year")
    elif year % 100 != 0:
        print("leap year")
    elif year % 400 != 0:
        print("common year")
    else:
        print("leap year")
