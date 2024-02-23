import pandas as pd                                  #importing  necessary modules
import smtplib

df=pd.read_excel("C:/Users/imran/OneDrive/Desktop/Book1.xlsx")  # reading emails from dataset 
df1=df['Email'].tolist()                                        #converting dataframe into list using tolist()

sender ='hippiehappy98@gmail.com'                               # storing to_address/sender mail id in a variable

mail= smtplib.SMTP('smtp.gmail.com',587)                        # smptplib port details 
mail.starttls()                                                 # securing transaction layer
mail.login(sender,'enter password')                             # enetr login credentials
mail.sendmail(sender,df1,'Type your message')                   # pass sendermail id, recepient mail id , "type the  message"

