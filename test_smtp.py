import smtplib
import os
from dotenv import load_dotenv

load_dotenv()

SMTP_USER = os.environ.get("SMTP_USER", "")
SMTP_PASS = os.environ.get("SMTP_PASS", "")
SMTP_FROM = os.environ.get("SMTP_FROM", "")

print(f"SMTP_USER: {SMTP_USER}")
print(f"SMTP_PASS: {SMTP_PASS[:4]}{'*' * (len(SMTP_PASS)-4)}")
print(f"SMTP_FROM: {SMTP_FROM}")

try:
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(SMTP_USER, SMTP_PASS)
    print("✅ LOGIN SUCCESSFUL!")
    server.quit()
except Exception as e:
    print(f"❌ FAILED: {e}")