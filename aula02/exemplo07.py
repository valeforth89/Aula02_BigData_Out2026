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

# Cálculo de aumento salarial

# Entrada
preco = float(input("Informe o preço: "))
quantidade = int(input("Informe a quantidade: "))

#Processamento
sub_total = preco * quantidade
desconto = sub_total * 0.1
total = sub_total - desconto

# Saída
print (f"\nO Valor total é: R$ {sub_total} \nDesconto de R$: {desconto} \nTotal com desconto R$: {total}")