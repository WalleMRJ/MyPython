####################################################
# MC102 -  Algoritmos e Programação de Computador
# Laboratório 2 - Noite de Sono
# Nome:
# RA:
####################################################

# Leitura de dados

h_1 = int(input("Digite a hora que irá dormir: ")) #Capturando dados inteiros do usuário
m_1 = int(input("Digite os minutos que irá dormir: ")) #Capturando dados inteiros do usuário
h_2 = int(input("Digite a hora para despertar: ")) #Capturando dados inteiros do usuário
m_2 = int(input("Digite os minutos para despertar: ")) #Capturando dados inteiros do usuário

boa_noite = True #Váriavel com valor inicial verdadeiro
condicao1 = 0 #Variável com valor inicial em 0
x = 0 #Variável com valor inicial em 0

# Cálculo de tempo dormindo
if h_1 > h_2: #Se a hora de dormir for maior que a hora de acordar.
    x = 24 - h_1 #x será atualizado para 24horas menos a hora de dormir.
    condicao1 = x + h_2 #x será somado a hora de despetar.

if m_1 > m_2: #Se o minuto de ir dormir for maior que o minuto de despetar
    condicao1 -= 1 #Subtraindo 1 hora caso a condição anterior seja realizada.
elif h_1 < h_2 : #Hora de dormir menor que a hora de despetar.
    condicao1 = h_2 - h_1 #Substrai hora de despetar pela hora de acordar.

if condicao1 >= 8: #Se o resultado dessas condições der maior ou igual a 8 horas será Verdadeiro.
    print(boa_noite) #Impressão de resposta True.
else:
    boa_noite = False #Se o resultado anterior for menor que 8 horas será Falso.
    print(boa_noite) #Impressão de resposta False.
