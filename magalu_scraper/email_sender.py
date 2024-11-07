import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders


def send_email():
    # Configurações do e-mail
    sender_email = "seuemail@gmail.com"
    receiver_email = "destinatario@example.com"
    password = "senha_do_app"

    
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = "Relatório de Notebooks"
    
    body = "Olá, aqui está o seu relatório dos notebooks extraídos da Magazine Luiza.\n\nAtenciosamente,\n\nRobô"
    msg.attach(MIMEText(body, 'plain'))

    file_path = "output/notebooks.xlsx"

    try:
        with open(file_path, "rb") as attachment:
            mime_base = MIMEBase('application', 'octet-stream')
            mime_base.set_payload(attachment.read())
            encoders.encode_base64(mime_base)
            mime_base.add_header('Content-Disposition', 'attachment; filename=notebook.xlsx')
            msg.attach(mime_base)
    except FileNotFoundError:
        print("Erro: O arquivo não foi encontrado.")
        return
    
    try:
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()
            server.login(sender_email, password)
            text = msg.as_string()
            server.sendmail(sender_email, receiver_email, text)
            print("E-mail enviado com sucesso!")
    except Exception as e:
        print(f"Erro ao enviar o e-mail: {e}")
