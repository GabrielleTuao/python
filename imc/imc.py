def main():
    try:
        # input sempre se entende como texto, por isso deve ser convertido
        peso = input("Digite o seu peso em quilos: ")
        peso = float(peso)
        altura = float(input("Digite a sua altura em metros: 70"))

    except ValueError:
        print("O valor fornecido não é válido!")
        return

    imc = peso / altura ** 2

    print(imc)
    

main()
