import os # Verifica o sistema e limpa a tela
''''''
# os.name =='nt' identifica se o sistema é Windows, executando o comando o comando 'cls' para limpar a tela. 
# Caso contrário (else), para sistemas Linux ou Mac (baseados em Unix), o comando 'clear' é utilizado.
# os.name == 'nt' significa que o sistema operacional é Windows, enquanto 'posix' indica Linux ou Mac.
# os.name retorna 'nt' para Windows e 'posix' para Linux/Mac
''''''
if os.name == 'nt':  # Windows
    os.system('cls')
else:  # Linux/Mac
    os.system('clear')
# Início do programa:
# Este programa calcula o valor final da sua compra com base em descontos progressivos.
print("#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#")
print("Bem-vindo ao Sistema de Desconto Progressivo!")
print("#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#")
# Entrada de dados pelo usuário. 
# Solicita ao usuário que insira o valor total da sua compra.
vltotal = float(input("Digite o valor total da sua compra (utilize ponto no lugar da vírgula): R$ "))
# Processamento dos dados
# Calcula os valores com desconto progressivo com base no valor total da compra.
reduz5= vltotal * 0.05
reduz10= vltotal * 0.1
reduz15= vltotal * 0.15
# Calcula os valores finais após aplicar os descontos.
desconto5 = vltotal - reduz5
desconto10 = vltotal - reduz10
desconto15 = vltotal - reduz15
# Saída de dados com base no valor total da compra.
# Saída usando f-string com formatação para exibir os valores com desconto e a economia obtida.
if vltotal < 200.00:
    print(f"O valor atual da sua compra é R$ {desconto5:.2f}.\n"
        f"Você receberá um desconto de 5% sobre o valor total da sua compra.\n"
        f"E você economizará R$ {reduz5:.2f}.")
elif 200.00 <= vltotal < 300.00:
    print(f"O valor atual da sua compra é R$ {desconto10:.2f}.\n"
        f"Você receberá um desconto de 10% sobre o valor total da sua compra.\n"
        f"E você economizará R$ {reduz10:.2f}.")
else:
    print(f"O valor atual da sua compra é R$ {desconto15:.2f}.\n"
        f"Você receberá um desconto de 15% sobre o valor total da sua compra.\n"
        f"E você economizará R$ {reduz15:.2f}.") 
# Finalização do programa.