import datetime

# Obtém a data e hora atuais
agora = datetime.datetime.now()

hora = agora.hour

if hora >= 6 and hora < 12:
    print("Bom dia amigo!")
elif hora >= 12 and hora < 18:
    print("Boa tarde amigo!")
elif hora >= 18 and hora < 24:
    print("Boa noite amigo!")
else:  # hora >= 0 and hora < 6
    print("Boa madrugada amigo!")

# Exibe a data e hora atual
print("Data e hora atual:", agora)

# Exibe apenas a hora atual
print("Hora atual:", agora.hour)

# Exibe apenas os minutos atuais
print("Minutos atuais:", agora.minute)

# Exibe apenas os segundos atuais
print("Segundos atuais:", agora.second)