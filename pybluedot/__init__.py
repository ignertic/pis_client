from .bluedot import Bluedot


__version__= "0.1.0"



@client.send("Sender Name")
def send(result): #result -> msg and phone
    result.balance
    print("Ok")

#check balance 
recipients = ["270000", "2132123"]
msg = "Hi guys"
pkg = {"recipients" : ["07844426662", "902013123"], "msg" : "Hi guys"}
send(pkg)
