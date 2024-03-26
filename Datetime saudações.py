import datetime

# Obtém a data e hora atuais
agora = datetime.datetime.now()

hora = agora.hour

if hora < 0 or hora > 23:
    print("Horario invalido!")
else:
    if hora >= 12 and hora < 18:
        print("Boa tarde amigo!")
    elif hora < 12:
        print("Bom dia amigo!")
    else:
        print("Boa noite amigo!")

# Exibe a data e hora atual
print("Data e hora atual:", agora)

# Exibe apenas a hora atual
print("Hora atual:", agora.hour)

# Exibe apenas os minutos atuais
print("Minutos atuais:", agora.minute)

# Exibe apenas os segundos atuais
print("Segundos atuais:", agora.second)

