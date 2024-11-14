#idade
import datetime
data_atual = datetime.date.today()
ano_atual = data_atual.year
nome = input("informe o Nome: ")
n1 = int(input("Ano de Nascimento: "))
idade = ano_atual - n1 
print(f"A Idade de {nome} é de {idade} anos")

