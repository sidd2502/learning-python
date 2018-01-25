import twilio
import twilio.rest
from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "AC1438164abc3111cdbc3461583ccd8abc"
# Your Auth Token from twilio.com/console
auth_token  = "32e7211474787aee6c26eede0a9477c0"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+919873007620", 
    from_="+12133352394",
    body="Dear Giznu, sending you message from a program written by me")

print(message.sid)
