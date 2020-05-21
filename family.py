from twilio.rest import Client


account_sid = "AC65719dc6a742453f540e7d19b2b743d1"
auth_token = "[Auth Token]"
client = Client(account_sid, auth_token)


def send_news():

    message = client.messages.create(
        from_="whatsapp:[your_twilio_number]",
        body="[your messages].",
        to="whatsapp:[your_target_number]",
    )

    print(message.sid)
