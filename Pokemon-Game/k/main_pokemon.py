from k.bubassauro import Bubassaur
from k.ivysaurr import Ivysaur

def Comparar(A, B):
    return A > B
    

bubassauro1 = Bubassaur(attack = 30, defense = 30, level = 1, evolucao_ant= 'None', evolucao_pos = 'Ivysaur', hp = 30)

bubassauro2 = Bubassaur(attack = 30, defense = 30, level = 2, evolucao_ant= 'None', evolucao_pos = 'Ivysaur', hp = 30)

print(bubassauro1)
print(bubassauro2)

ataqueB1 = bubassauro1.attack()
defesaB2 = bubassauro2.defense()

b1_Maior_b2 =  Comparar(ataqueB1, defesaB2)

print('Valor de ataque B1: {}\n'.format(ataqueB1))

print('Valor de defesa B2: {}\n'.format(defesaB2))

if b1_Maior_b2:
    print('Bubassauro 1 venceu!')

else:
    print('Bubassauro 2 venceu')

# ------------------------------------------------

ivysaur = Ivysaur(attack = 40, defense = 40, level = 2)

defesa_ivy = ivysaur.defense()

b1_maior_ivy = Comparar(ataqueB1, defesa_ivy)

defesa_ivy = ivysaur.defense()

print('Valor de ataque Bubassauro: {}\n'.format(ataqueB1))

print('Valor de defesa Ivy: {}\n'.format(defesa_ivy))

if b1_maior_ivy:
    print('Bubassauro venceu!')

else:
    print('Ivy venceu')


