import imaplib
import email

# Conectar ao servidor
imap = imaplib.IMAP4_SSL("imap.gmail.com")
# Fazer login
imap.login("seuemail@gmail.com", "suasenha")
# Selecionar caixa de entrada
imap.select("inbox")

# Buscar e-mails não lidos
status, emails = imap.search(None, "(UNSEEN)")

# Criar um dicionário vazio para armazenar os assuntos e corpos dos e-mails
email_dict = {}

# Obter todos os corpos e assuntos dos emails e adicionar no dicionário
for email_id in emails[0].split():
    status, email_data = imap.fetch(email_id, "(RFC822)")
    email_message = email.message_from_bytes(email_data[0][1])
    subject = email_message["Subject"]
    body = email_message.get_payload()[0].get_payload()
    email_dict[subject] = body

# Fechar a conexão com o servidor IMAP
imap.close()
imap.logout()

#Imprimir dicionário
print(email_dict)