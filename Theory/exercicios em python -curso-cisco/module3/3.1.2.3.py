
# o magico precisa de sua ajuda para fazer seu desafio rodar , sua missao e fazer o codigo rodar enquanto o usuario nao advinhar o numero misterioso ! bom show



secret_number = 777

print(
"""
+================================+
| Welcome to my game, muggle!    |
| Enter an integer number        |
| and guess what number I've     |
| picked for you.                |
| So, what is the secret number? |
+================================+
""")

number_p = int(input("informe o nume que estou pensando se for capaz !   "))
while secret_number:
   
    if secret_number != number_p :
       
       print(
"""
+================================+
|Ha ha! You're stuck in my loop!|
+================================+
""")     
    else: 
        print(
"""
+================================+
|Well done, muggle! You are free |
|             now!               |
+================================+
""")  
