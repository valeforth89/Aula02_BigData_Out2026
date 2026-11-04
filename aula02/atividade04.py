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
sal_atual = float(input("Informe o salário atual: "))
aumento_perc = 0.15

# Processamento
aumento = float(sal_atual * aumento_perc)
novo_sal = float(sal_atual + aumento)

# Saída
print (f"\nSalário atual: R$ {sal_atual} \nCom o aumento de: R$ {aumento:.2f} \nO novo salário será: R$ {novo_sal:.2f}")