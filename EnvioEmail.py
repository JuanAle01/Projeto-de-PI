import smtplib  # biblioteca send mail transfer protocol
import ssl  # biblioteca para conexão segura no acesso do e-mail
# biblioteca para configurar mensagem de e-mail
from email.message import EmailMessage

email = ('')  # e-mail remetente
email_password = ('')  # senha do e-mail

# cria requisição do e-mail
msg = EmailMessage()
msg['Subject'] = "Assunto"  # Assunto do e-mail
msg['From'] = ''  # Remetente do e-mail
msg['To'] = ''  # Desinatário do e-mail
msg.set_content('Testeee ')  # Corpo da mensagem

context = ssl.create_default_context()
# Conexão ao e-mail e protocolo
# especifica o tipo de envio no SMTP e qual porta deve ser acessada
with smtplib.SMTP("smtp.gmail.com", port=587) as smtp:
    smtp.starttls(context=context)  # coneta seguramente ao TLS
    # captura o e-mail (from) e adiciona a senha
    smtp.login(msg['From'], "workspace123")
    smtp.send_message(msg)  # envia a mensagem
    # Credenciais de Log in para enviar o e-mail

    # smtp.login(email, email_password) # realiza o log-in (forma de enviar utilizando variáveis)