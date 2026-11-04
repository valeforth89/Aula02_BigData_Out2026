# input = entrada
# print = saída
# print (f) = concatenar saída de texto com variável
# int () = converte entrada para int (Inteiro)
# type = retorna o tipo da variável
# variavel:.2f = limita a saída dos caracteres para, no exemplo, 2 casas decimais

# Tipos de variáveis:
    # int = número inteiro (ex.: idade = 18)
    # float = número real/fracionário (ex.: Altura = 1.79)
    # str = string texto (ex.: "TEXTO")
    # boolean = válores lógicos (ex.: TRUE ou FALSE)

# Cálculo do valor de uma corrida de táxi

taxa_fixa = 8
preco_km = 3
taxa_servico = 5

# Entrada
km_percorrido = float(input("Distância Percorrida: "))
passageiros = int(input("Quantos Passageiros? "))

#Processamento
valor_total = (km_percorrido * preco_km) + taxa_fixa + taxa_servico
valor_passageiro = valor_total / passageiros

# Saída
print (f"\nO valor total da corrida ficou em: R$ {valor_total:.2f} \nDivido por: {passageiros} passageiros \nO Valor dividido da conta é: R$ {valor_passageiro:.2f} por pessoa")