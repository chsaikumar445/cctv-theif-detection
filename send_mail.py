import os
import smtplib
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart




fromaddr = "myapptest525@gmail.com"
password = "6302649445sS@"

def SendMail(ImgFileName):
    with open(ImgFileName, 'rb') as f:
        img_data = f.read()

    msg = MIMEMultipart()
    msg['Subject'] = 'subject'
    msg['From'] = '@mail.cc'
    msg['To'] = fromaddr

    text = MIMEText("test")
    msg.attach(text)
    image = MIMEImage(img_data, name=os.path.basename(ImgFileName))
    msg.attach(image)

    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.ehlo()
    s.starttls()
    s.ehlo()
    s.login(fromaddr, password)
    s.sendmail(fromaddr, fromaddr, msg.as_string())
    print("Mail send successfully.")
    s.quit()


SendMail("img1.png")