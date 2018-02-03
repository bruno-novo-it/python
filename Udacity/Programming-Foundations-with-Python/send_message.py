
# https://www.twilio.com/console

from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "AC36625386a5d11b413dc97001d6c088ba"
# Your Auth Token from twilio.com/console
auth_token  = "Get in the Above Site =)"

client = Client(account_sid, auth_token)

message = client.messages.create(
    body="Agora Vaaai Papaaaaai!",
    to="+5511966697975", 
    from_="+18555076830")

print(message.sid)