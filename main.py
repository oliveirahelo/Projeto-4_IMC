try:  #código que pode gerar o erro
    nome = input("Digite seu nome: ")  
    altura = float(input("Digite sua altura: "))
    peso = float(input("Digite seu peso: "))

    imc = peso / (altura * altura)

    if imc < 18.5:
        print("Abaixo do peso")
    elif imc >= 18.5 and imc <= 24.9:
        print("Peso normal")
    elif imc >= 25.0 and imc <= 29.9:
        print("Sobrepeso")
    elif imc >= 30.0 and imc <= 34.9:
     print("Obesidade grau I")
    elif imc >= 35.0 and imc <= 39.9:
        print("Obesidade grau II")
    else:
        print("Obesidade grau III")

    print(f"O nome do paciente é: {nome}, e seu IMC é: {imc}")

except ValueError:  #o que fazer se o erro acontecer
    print("Erro: altura e peso devem ser números.")
except ZeroDivisionError:
    print("Erro: altura não pode ser zero.")
except Exception as e:
    print(f"Ocorreu um erro inesperado: {e}")
    
with open ("cadastro_imc.txt" , "a") as arquivo:
    arquivo.write (f"Nome: {nome}\nIMC: {imc: .2f}")
    
    
#O que mudou:
# Usamos try para proteger toda a lógica de entrada e cálculo.
#Usamos except ValueError para tratar entradas não numéricas.
#Usamos except ZeroDivisionError para garantir que altura ≠ 0.
#Você também pode usar while para repetir até o usuário digitar corretamente