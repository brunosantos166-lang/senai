#  Print de boas-vindas com meu nome
print(" Bem-vindo ao Sistema de Acesso ")

#  Coleta de dados do usuário
tipo_usuario = input("Você é 'membro' ou 'visitante'? ").strip().lower()
dia_semana = input("Qual o dia da semana? (segunda a domingo): ").strip().lower()
hora_atual = int(input("Qual a hora atual ?  "))

# Variável auxiliar para controlar a permissão
acesso_permitido = False
motivo_negativa = ""

# Lógica principal usando estruturas condicionais (D e E)
if dia_semana in ['sábado', 'sabado', 'domingo']:
    # Regra para fins de semana: Apenas membros entram
    if tipo_usuario == 'membro':
        acesso_permitido = True
    else:
        motivo_negativa = "Visitantes não têm acesso aos fins de semana."

elif dia_semana in ['segunda', 'terça', 'terca', 'quarta', 'quinta', 'sexta']:
    # Regra para dias úteis: Verificar horário comercial (9h às 18h)
    if 9 <= hora_atual < 18:
        if tipo_usuario == 'membro':
            # Membros têm acesso ilimitado no horário comercial
            acesso_permitido = True
        elif tipo_usuario == 'visitante':
            # Visitantes precisam informar o tempo e respeitar o limite de 4h
            tempo_permanencia = int(input("Quanto tempo deseja permanecer? (horas inteiras): "))
            
            if tempo_permanencia <= 4:
                # Verifica se o tempo de permanência não ultrapassa o fechamento (18h)
                if hora_atual + tempo_permanencia <= 18:
                    acesso_permitido = True
                else:
                    motivo_negativa = "O tempo de permanência ultrapassa o horário de fechamento (18h)."
            else:
                motivo_negativa = "Visitantes podem permanecer no máximo 4 horas."
        else:
            motivo_negativa = "Tipo de usuário inválido."
    else:
        motivo_negativa = "O espaço está fechado. Horário comercial: 09h às 18h."
else:
    motivo_negativa = "Dia da semana inválido."

# F. Apresentação do resultado no console
print("\n Resultado do Acesso ")
if acesso_permitido:
    print(" ACESSO PERMITIDO. Seja bem-vindo!")
else:
    print(f" ACESSO NEGADO. Motivo: {motivo_negativa}")