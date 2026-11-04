# input = entrada
# print = saída
# print (f) = concatenar saída de texto com variável
# int () = converte entrada para int (Inteiro)
# type = retorna o tipo da variável

# Tipos de variáveis:
    # int = número inteiro (ex.: idade = 18)
    # float = número real/fracionário (ex.: Altura = 1.79)
    # str = string texto (ex.: "TEXTO")
    # boolean = válores lógicos (ex.: TRUE ou FALSE)

# Valor de uma compra

# Entrada
preco = float(input("Informe o preço: "))
quantidade = int(input("Informe a quantidade: "))

#Processamento
total = preco * quantidade

# Saída
print (f"O Valor total é: R$ {total}")
