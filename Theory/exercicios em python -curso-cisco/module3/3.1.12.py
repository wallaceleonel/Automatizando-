#tendo como objetivo calcular o imposto da cidade com os valores fornecidos #pelo sistema
#objetico era ultilizar os comandos input, if ,elif,else e por em pratica a #logica de programação 

ncome = float(input("Enter the annual income: "))
if income <85528:
    tax = income *0.18 -556.02
else:
    tax : (income-85528)*0.32 + 14839.02
if tax <0.0:
    tax= 0.0
tax = round(tax, 0)
print("The tax is:", tax, "thalers")
