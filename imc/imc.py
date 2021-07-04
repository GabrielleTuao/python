escala_imc={ #dicionario no python
    "map":"muito abaixo do peso",
    "ap": "abaixo do peso",
    "pi":"peso ideal",
    "ac": "acima do peso",
    "o1":"obesidade 1",
    "o2":"obesidade 2",
    "o3":"obesidade 3"
}
#tupla é um tipo container parecido com lista em que os elementos são indexados
def calcular_imc(peso_kg: float, altura_m: float) -> tuple[float, str]: #tupla é um tipo container especificado entre parenteses no return

    imc = peso_kg / altura_m ** 2

     if imc < 17:
        situacao = "map"
    elif imc < 18.5:  #else if senão se
        sutuacao = "ap"
    elif imc < 25:
        situacao = "pi"
    elif imc < 30:
        situacao = "ac"
    elif imc < 35:
        situacao = "o1"
    elif imc < 40:
        situacao = "o2"
    else: 
        situacao = "o3"
    
    return (imc, situacao)


def main():
    try:
        # input sempre se entende como texto, por isso deve ser convertido
        peso = input("Digite o seu peso em quilos: ")
        peso = float(peso)
        altura = float(input("Digite a sua altura em metros: "))

    except ValueError:
        print("O valor fornecido não é válido!")
        return
  

    print("Seu IMC é",imc)
    print("Sua situação é", situacao)
    

main()
