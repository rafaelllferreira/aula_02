#prestação
prestacao = float(input("Valor prestação: "))
taxa = float(input("taxa Mensal: "))
tempo = float(input("Quantidade de meses em atraso: "))
valorfinal = prestacao+(prestacao*(taxa/100)*tempo)
print(f"o valor final da prestação é R${valorfinal:.2F}")