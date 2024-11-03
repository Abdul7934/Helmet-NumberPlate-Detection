from twilio.rest import Client

def send_alert(message, phone_number):
    # Twilio integration for sending alerts
    account_sid = 'your_account_sid'
    auth_token = 'your_auth_token'
    client = Client(account_sid, auth_token)

    client.messages.create(
        body=message,
        from_='your_twilio_phone_number',
        to=phone_number
    )
