def celsius_to_kelvin(x):
    k = x+273
    return k

def celsius_to_fahren(x):
    f = (x*1.8)+32
    return f

def kelvin_to_celsius(x):
    c = x-273
    return c

def kelvin_to_fahren(x):
    f = ((x-273)*1.8)+32
    return f

def fahren_to_celsius(x):
    c = (x-32)/1.8
    return c

def fahren_to_kelvin(x):
    k = ((x-32)*5/9)+273
    return k


print("Digite os valores abaixo até no máximo 2 casas decimais.")
cel = float(input("Digite uma temperatura em graus Celsius:"))
fah = float(input("Digite uma temperatura em Fahrenheit:"))
kel = float(input("Digite uma temperatura em Kelvin:"))
print(f"\nTemperatura digitada em graus Celsius: {cel:.2f}º.")
print(f"Temperatura digitada em Fahrenheit: {fah:.2f}f.")
print(f"Temperatura digitada em Kelvin: {kel:.2f}k.")

c_to_f = celsius_to_fahren(cel)
c_to_k = celsius_to_kelvin(cel)
f_to_c = fahren_to_celsius(fah)
f_to_k = fahren_to_kelvin(fah)
k_to_c = kelvin_to_celsius(kel)
k_to_f = kelvin_to_fahren(kel)

print(f"\nTemperatura em Celsius foi de {cel:.2f} para {c_to_f:.2f}f.")
print(f"Temperatura em Celsius foi de {cel:.2f} para {c_to_k:.2f}k.")
print(f"Temperatura em Fahrenheit foi de {fah:.2f} para {f_to_c:.2f}º.")
print(f"Temperatura em Fahrenheit foi de {fah:.2f} para {f_to_k:.2f}k.")
print(f"Temperatura em Kelvin foi de {kel:.2f} para {k_to_c:.2f}º.")
print(f"Temperatura em Kelvin foi de {kel:.2f} para {k_to_f:.2f}f.")

sair = ""
while sair != "sim":
    print("\n**Os Valores selecionados para serem os valores de ''baixo, média e alto'' foram escolhidos aleatoriamente.**")
    print("**Os Valores selecionados para serem os valores de ''Celsius, Fahrenheit e Celsius'' foram selecionados\nos valores ditos primeiramente, sem contar os da conversão.**")
    escolha = (input("\nEscolha um dos tipos de temperatura para verificar a categoria dela:\n (Celsius, Fahrenheit ou Kelvin)"))
    if(escolha == "Celsius"):
            if(cel < 10.0):
                print("A temperatura em Celsius está abaixo da média.")
            elif(cel >= 10 and cel < 30):
                print("A temperatura em Celsius está na média.")
            elif(cel >= 30 and cel <60):
                print("A temperatura em Celsius está acima da média.")
            elif(cel >= 60):
                print("Temperatura em Celsius extremamente alta, você está bem? Recomendo procurar um local com menor temperatura.")
    elif(escolha == "Fahrenheit"):
            if(fah < 50):
                print("A temperatura em Fahrenheit está abaixo da média.")
            elif(fah >= 50 and fah < 86):
                print("A temperatura em Fahrenheit está na média.")
            elif(fah >= 86 and fah < 120):
                print("A temperatura em Fahrenheit está acima da média.")
            elif(fah >= 120):
                print("Temperatura em Fahrenheit extremamente alta, você está bem? Recomendo procurar um local com menor temperatura.")
    elif(escolha == "Kelvin"):
            if(kel < 283):
                print("A temperatura em Kelvin está abaixo da média.")
            elif(kel >= 283 and kel < 303):
                print("A temperatura em Kelvin está na média.")
            elif(kel >= 303 and kel < 330):
                print("A temperatura em Kelvin está acima da média.")
            elif(kel >= 330):
                print("Temperatura em Kelvin estremamente alta, você está bem? Recomendo procurar um local com menor temperatura.")
    else:
        print("Escolha errada/inválida. Por favor digite um tipo de temperatura citado acima! Ou seu computador irá explodir por conta da alta temperatura(bricadeira).")
    sair = input("Deseja finalizar? Caso sim, digite sim e, caso não digite qualquer outra coisa diferente de sim: ").lower()
print("Programa finalizado. Seja no frio ou no calor, tenha um ótimo dia!")
