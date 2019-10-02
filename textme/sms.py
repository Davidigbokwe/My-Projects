from twilio.rest import Client


# Your Account Sid and Auth Token from twilio.com/console
# DANGER! This is insecure. See http://twil.io/secure
account_sid = 'ACd827e693bc855daa5113c5d2d4f6c9c3'
auth_token = 'f564dc265c488481f28b639a039538f9'
client = Client(account_sid, auth_token)

message = client.messages.create(
                              body="I can't believe this works!",
                              from_='+12052458750',
                              to='+2348056679806'
                          )

print(message.sid)
