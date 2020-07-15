def send_email(title, content):
    import smtplib
    from email.mime.multipart import MIMEMultipart
    from email.mime.text import MIMEText
    mail_host = 'smtp.163.com'
    mail_user = '15521505144@163.com'

    # 这个是授权码 不是密码 需要去163设置
    mail_pass = 'AVIGHTZYNSINDXZX'
    sender = '15521505144@163.com'
    receivers = ['635816807@qq.com']

    # 构造message （邮件内容）
    message = MIMEText(content, 'plain', 'utf-8')
    message['Subject'] = title
    message['From'] = sender
    message['To'] = receivers[0]

    # smtp = smtplib.SMTP(mail_host, 587)
    try:
        # smtp = smtplib.SMTP_SSL(mail_host, 465)  # 启用SSL发信, 端口一般是465

        smtp = smtplib.SMTP()
        smtp.connect(mail_host)
        smtp.set_debuglevel(1)
        smtp.ehlo()
        # smtp.starttls()
        smtp.ehlo()
        smtp.login(mail_user, mail_pass)
        smtp.sendmail(sender, receivers, message.as_string())
        smtp.quit()
        print("mail has been send successfully.")
    except smtplib.SMTPException as e:
        print(e)