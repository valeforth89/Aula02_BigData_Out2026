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

# Divisão da conta

# Entrada
total_conta = float(input("Informe o total da conta: "))
pessoas = int(input("Quantas pessoas participaram? "))

#Processamento
divisao = total_conta / pessoas

# Saída
print (f"\nTotal da conta: R$ {total_conta} \nDivido por: {pessoas} \nO Valor dividido da conta é: R$ {divisao:.2f} por pessoa")