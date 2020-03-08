import smtplib, socket, datetime
from email.mime.multipart import MIMEMultipart 
from email.mime.text import MIMEText  
slave_sender = 'pembamoktan.t@gmail.com'
slave_passwd = 'D1i1s1m1i1s@'
receiver = 'pembatamang.m@gmail.com'
wish = '\t\t\tDISMIS\nHello I am Dismis, a virtual assistance program designed and programed by Mr PEMBA. \nHappy Birthday Miss Anisha! God Bless You. Have a awsome day Miss Anisha. \nA great future is await for you Miss Anisha.'
while True:
    start_time = datetime.datetime(2020,3,8,13,00) 
    #start_time = datetime.datetime(2021,3,2) 
    if datetime.datetime.now() == start_time:
        #२०७७ फागुन १८
        try:
            msg = MIMEMultipart()
            msg['From'] = slave_sender
            msg['To'] = receiver
            msg['Subject'] = 'Anisha Limbu aka Distu Tamatar\'s Birthday!'
            body = wish
            msg.attach(MIMEText(body,'plain'))
            server = smtplib.SMTP('smtp.gmail.com:587')
            server.starttls()
            server.ehlo()
            server.login(slave_sender, slave_passwd)
            server.sendmail(slave_sender, receiver, msg.as_string())
            server.quit()
            print('--- Birthday wish of Anisha send successfully boss! ---')
        except socket.gaierror:
            pass
        break


#while True:
#    current_time = datetime.now().strftime("%H:%M:%S")
#    if current_time == "14:41:25":
#        print("alarm", "this is the message")
#        break
#    else:
#        pass