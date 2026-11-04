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

# Divisão Pizzaria


# Entrada
valor_total = 120
quantidade = int(input("Informe a quantidade de pessoas: "))

#Processamento
divisao = valor_total / quantidade

# Saída
print (f"\nO Valor total da conta é: R$ {valor_total} \nDividido por: {quantidade} pessoas \nTotal por pessoa R$: {divisao}")
