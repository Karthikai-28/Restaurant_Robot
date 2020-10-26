import smtplib

server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
server.login("restaurantrobot01@gmail.com", "Stumbleupon01")
server.sendmail("restaurantrobot01@gmail.com", "kk28296@gmail.com", "*Chuckles* I'm screwed")

server.quit()

