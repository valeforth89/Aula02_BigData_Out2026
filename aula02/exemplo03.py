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


# Entrada
ano_atual = 2026

nome = input ("Nome: ")
ano_nasc = int (input ("Ano de Nascimento: "))

# Processamento
idade = ano_atual - ano_nasc

# Saída
print (f"\nOlá, {nome}\n{idade} anos")
