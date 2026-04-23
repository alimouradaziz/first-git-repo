import yagmail

EMAIL_USER = "mayaj.lerma@gmail.com"
EMAIL_APP_PASSWORD = "hzzs tgew kztq lhwn"
EMAIL_TO = "amouradaziz@gmail.com"

try:
    yag = yagmail.SMTP(
        user=EMAIL_USER,
        password=EMAIL_APP_PASSWORD,
        host="smtp.gmail.com"
    )

    yag.send(
        to=EMAIL_TO,
        subject="Nur el Donya Test Email",
        contents="This is a direct test email from the Raspberry Pi."
    )

    print("Direct email test sent successfully")

except Exception as e:
    print("Direct email test failed:", e)