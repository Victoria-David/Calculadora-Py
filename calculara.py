#Calculadora de Aprovação Escolar

nome = input("Digite o nome do estudante: ")

soma_nota = 0
quantidade_trimestre = 3
meta_apreovacao = 180

#coleta as notas dos 3 períodos
for i in range(1, quantidade_trimestre + 1):
    nota = floot(input("Informe a nota{i}º período"))
soma_notas +=nota

print("-" * 30) 
print(f"Estudante: {nome}")
print(f"Pontuacao Total: {soma_notas}
")

#Verifica o Status de aprovação
if soma_notas >= meta_apreovacao:
print("Status: APROVADÃO! PARABENS!! FINALMENTE!!")
else:
    pontos_faltantes = meta_apreovacao - soma_notas
    print("status: TENTE OUTRA VEZ!!")
    print(f"Faltaram {pontos_faltantes} pontos para atingir o mínimo de {meta_aprovacao}. ")