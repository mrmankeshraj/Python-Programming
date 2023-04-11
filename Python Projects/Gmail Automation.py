import smtplib as s

ob = s.SMTP("smtp.gmail.com", 587)
ob.ehlo()
ob.starttls()
ob.login("mankeshraj.navavision@gmail.com", "gataca321") 
subject = "Test Python"
body = "I love Python"
message = "subject:{}\n\n{}".format(subject, body)
listadd = ["mrmankeshraj@gmail.com"]
ob.sendmail("mankeshraj.navavision@gmail.com", listadd, message)
print("Email Sent")
ob.quit()