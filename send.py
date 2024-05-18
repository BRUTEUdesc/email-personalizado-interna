import sys
import smtplib

# Descomentar a parte do final (que realmente manda os emails) somente apos os devidos testes e quando tiver
# certeza da corretude.

# Ler csv

# Propriedades importantes do csv:
# A coluna C (index 2) eh o nome do time
# A coluna D (index 3) eh se o time eh 'Presencial' ou 'Online'
# As colunas H,I,J (indexes 7, 8 e 9) sao os emails dos 3 competidores

fst = input()
emails = []
names = []
for line in sys.stdin:
    arr = line.split(",")
    if arr[3]!='Presencial':
        continue
    emails.append(arr[7:10])
    names.append(arr[2])
    cur = 0

# Detalhes de login e assunto do email
# Obs: gerar "app password" na conta do google para usar

subject = "Maratona Interna - UDESC"
user = "**********@gmail.com"
password = "*****"

def send_email(recipient, subject, name):
    FROM = user
    TO = recipient if isinstance(recipient, list) else [recipient]
    TO_JOIN = ", ".join(TO)
    SUBJECT = subject
    TEXT = f'Olá,\n\nA inscrição do time {name} na Maratona está confirmada!\n\nFavor comparecer sábado na UDESC.\n\nTeremos um warmup às 10:00 para se familiarizar com o ambiente de prova, mas não é obrigatório comparecer.\n\nPara mais informações, acesse brute.joinville.udesc.br/inscricao\n\nBoa sorte!\n\nAtenciosamente\n\nEquipe BRUTE UDESC ­🎈'

    message = f'From: {FROM}\r\nTo: {TO_JOIN}\r\nSubject: {SUBJECT}\r\n{TEXT}'
    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(user, password)
        server.sendmail(FROM, TO, message.encode("utf8"))
        server.close()
        print(f'email para {TO_JOIN} enviado.')
    except:
        print('falha ao enviar email(!)')

# Descomentar quando tiver certeza da corretude!

#for i in range(len(names)):
#    if len(names[i])==0:
#        break
#    send_email(emails[i],subject,names[i])
