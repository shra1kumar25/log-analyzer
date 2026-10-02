from email_sender import send_email

alerts = [
    "ERROR: Database connection failed",
    "WARNING: Low disk space"
]

send_email(alerts)
