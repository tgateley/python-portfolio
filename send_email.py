import smtplib
import ssl

host = "smtp.gmail.com"
port = 465

username = "tgateley22@gmail.com"
password = "lgwrgbtaxiwrorth"

receiver = "tgateley@gmail.com"
context = ssl.create_default_context()

message = """Hi! This is a test email. """

with smtplib.SMTP_SSL(host, port, context=context) as server:
    server.login(username, password)
    server.sendmail(username, receiver, message)