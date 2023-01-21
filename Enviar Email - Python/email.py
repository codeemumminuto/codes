import smtplib

de = 'remetente@exemplo.com'
para = 'destinatario@exemplo.com'

# Dados do servidor
smtp_server = 'smtp.exemplo.com'
email = 'seu_email'
senha = 'sua_senha'

# Conexão
server = smtplib.SMTP(smtp_server)
server.starttls()
server.login(email, senha)

# Mensagem
assunto = 'assunto de email aleatório'
corpo = 'Corpo do e-mail teste'
mensagem = f'Subject: {assunto}\n\n{corpo}'

# Enviando o e-mail
server.sendmail(de, para, mensagem)

# Fechando a conexão
server.quit()
