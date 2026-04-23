last_email_event = None

def send_email(event):
    global last_email_event

    # Only send for important events
    if event not in ("KNOCK", "ALERT"):
        return

    if event == last_email_event:
        return

    try:
        if event == "KNOCK":
            subject = "Nur el Donya: Knock Detected"
            body = "Someone is knocking at your door."
        elif event == "ALERT":
            subject = "Nur el Donya: HIGH ALERT"
            body = "High-priority sound detected (possible alarm or emergency)."

        yag_mail.send(
            to=TO,
            subject=subject,
            contents=body
        )

        print("Email sent!")
        last_email_event = event

    except Exception as e:
        print("Email failed:", e)