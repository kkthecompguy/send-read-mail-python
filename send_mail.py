import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

host = "smtp.gmail.com"
username = "<youremailaddress>"
password =  "<yourpassword>"
port = 587

def send_mail(text="Email Body", subject="Thank You For Joining", to_emails=None, from_email=f"Python <{username}>", html=None):
    assert isinstance(to_emails, list)

    msg = MIMEMultipart('alternative')
    msg['From'] = from_email
    msg['To'] = ", ".join(to_emails)
    msg['Subject'] = subject

    text_part = MIMEText(text, 'plain')
    msg.attach(text_part)

    if html != None:
        html_part = MIMEText(html, 'html')
        msg.attach(html_part)

    msg_str = msg.as_string()

    with smtplib.SMTP(host, port) as server:
        server.ehlo()
        server.starttls()
        server.login(username, password)
        server.sendmail(from_email,to_emails, msg_str)

    # login into smtp server
    # server = smtplib.SMTP(host, port)
    # server.ehlo()
    # server.starttls()
    # server.login(username, password)
    # server.sendmail(from_email,to_emails, msg_str)
    # server.quit()
