import os
import smtplib
import tempfile
from src.config import GMAIL_USER, GMAIL_PASSWORD
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders


def load_data(df, date_str):
    with tempfile.NamedTemporaryFile(suffix=f"_{date_str}.csv", delete=False) as tmp_file:
        csv_path = tmp_file.name
        df.to_csv(csv_path, index=False)

    print(f"CSV saved at: {csv_path}")

    from_addr = GMAIL_USER
    to_addr = GMAIL_USER
    app_password = GMAIL_PASSWORD

    subject = f"Gold Data for {date_str}"
    body = f"""
    <h2>Daily Gold Data</h2>
    <p>Hello Dũng,</p>
    <p>Attached is your gold data for <b>{date_str}</b>.</p>
    """

    msg = MIMEMultipart()
    msg["From"] = from_addr
    msg["To"] = to_addr
    msg["Subject"] = subject
    msg.attach(MIMEText(body, "html"))

    with open(csv_path, "rb") as f:
        part = MIMEBase("application", "octet-stream")
        part.set_payload(f.read())

    encoders.encode_base64(part)
    part.add_header(
        "Content-Disposition",
        f"attachment; filename={os.path.basename(csv_path)}"
    )
    msg.attach(part)

    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login(from_addr, app_password)
            server.send_message(msg)
        print("Email sent successfully!")
    except Exception as e:
        print(f"Failed to send email: {e}")

    print("ETL Load stage complete.")
