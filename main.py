#imports
from twilio.rest import Client
from ast import  literal_eval 
from datetime import datetime,timezone
from pytz import timezone
from time import sleep

#opening  the text file which have credential and changing it into dict
with open("credential.txt",'r') as f:
    data_read = f.read()
    data_dict = literal_eval(data_read)

#passing credential
client = Client(data_dict['account'],data_dict['token'])
to_send={}

#whome to send message
to_send = dict({
    'mom':'xxxxxx',
    'dad':'xxxxxxxx',
    'myself':'xxxxxxxxx',
    'girlfriend':'xxxxxxx',
})

from_send = "+17026758616"

#message body
message_body = {}

message_body = dict({
    'mom':'I love you so muchhhh mom goodnight!',
    'girlfriend':'I don,t have one !',
    'myself':'You can do anything you are the best and best!',
    'dad':'Good night father have a wonderful sleep'
})


if  __name__ == "__main__":
    while True:
        #time
        time_format = "%H %M"

        time_utc = datetime.now(timezone('UTC'))

        time_nepal = time_utc.astimezone(timezone('Asia/Kathmandu'))

        final_time = time_nepal.strftime(time_format) 

        if str(final_time) == "21 30":                
            print("Enteted to sending loop")
            for i in to_send:
                if i == "mom":
                    try:
                        client.messages.create(to=to_send[i],from_=from_send,body=message_body[i])
                    except Exception as e:
                        print(f'Mom exception : {e}')
                
                if i == "dad":
                    try:
                        client.messages.create(to=to_send[i],from_=from_send,body=message_body[i])
                    except Exception as e:
                        print(f'Dad exception : {e}')
                

                if i == "girlfriend":
                    try:
                        client.messages.create(to=to_send[i],from_=from_send,body=message_body[i])
                    except Exception as e:
                        print(f'Girlfriend exception : {e}')
                if i == "myself":
                    try:
                        client.messages.create(to=to_send[i],from_=from_send,body=message_body[i])
                    except Exception as e:
                        print(f'Myself exception : {e}')

            sleep(62)
                
