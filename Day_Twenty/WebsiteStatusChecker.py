import requests
import tkinter as tk
from tkinter import messagebox, scrolledtext
import logging
import smtplib
from email.mime.text import MIMEText
from datetime import datetime

# Configure logging
LOG_FILE = "website_status.log"
logging.basicConfig(filename=LOG_FILE, level=logging.INFO,
                    format="%(asctime)s - %(message)s")

# Email Configuration (Update with your email credentials)
SMTP_SERVER = "smtp.gmail.com"  # Gmail SMTP
SMTP_PORT = 587
EMAIL_SENDER = "your_email@gmail.com"
EMAIL_PASSWORD = "your_app_password"
EMAIL_RECEIVER = "receiver_email@gmail.com"


def send_email_alert(url, status):
    """Send an email if a website is down."""
    try:
        subject = f"Website Down Alert: {url}"
        body = f"The website {url} is {status} as of {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
        msg = MIMEText(body)
        msg["Subject"] = subject
        msg["From"] = EMAIL_SENDER
        msg["To"] = EMAIL_RECEIVER

        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()
            server.login(EMAIL_SENDER, EMAIL_PASSWORD)
            server.sendmail(EMAIL_SENDER, EMAIL_RECEIVER, msg.as_string())

        logging.info(f"📧 Email sent for {url} being {status}")

    except Exception as e:
        logging.error(f"❌ Failed to send email: {e}")


def check_websites():
    """Check multiple websites entered by the user."""
    urls = url_entry.get("1.0", tk.END).strip().split(
        "\n")  # Get multiple URLs
    result_text.config(state=tk.NORMAL)  # Enable editing
    result_text.delete("1.0", tk.END)  # Clear previous results

    if not urls or urls == [""]:
        messagebox.showwarning(
            "Input Error", "Please enter at least one website URL")
        return

    for url in urls:
        url = url.strip()
        if not url:
            continue
        if not url.startswith("http"):
            url = "https://" + url  # Ensure the URL is complete

        try:
            response = requests.get(url, timeout=5)
            if response.status_code == 200:
                result = f"✅ {url} is Online"
                color = "green"
            else:
                result = f"⚠️ {url} returned status {response.status_code}"
                color = "orange"
        except requests.ConnectionError:
            result = f"❌ {url} is Offline"
            color = "red"
            send_email_alert(url, "Offline")
        except requests.Timeout:
            result = f"⚠️ {url} took too long to respond"
            color = "orange"
        except Exception as e:
            result = f"❌ Error checking {url}: {e}"
            color = "red"

        # Update GUI
        result_text.insert(tk.END, result + "\n", color)
        result_text.tag_config(color, foreground=color)

        # Log result
        logging.info(result)

    result_text.config(state=tk.DISABLED)  # Disable editing after update


# Create GUI Window
root = tk.Tk()
root.title("Website Status Checker")
root.geometry("500x400")

# Title Label
tk.Label(root, text="Enter Website URLs (One per line)",
         font=("Arial", 14)).pack(pady=10)

# Input Field (Scrolled Text for Multiple URLs)
url_entry = scrolledtext.ScrolledText(
    root, width=50, height=5, font=("Arial", 12))
url_entry.pack(pady=5)

# Check Button
check_button = tk.Button(root, text="Check Status", command=check_websites, font=(
    "Arial", 12), bg="blue", fg="white")
check_button.pack(pady=10)

# Status Label
result_text = scrolledtext.ScrolledText(
    root, width=50, height=10, font=("Arial", 12), state=tk.DISABLED)
result_text.pack(pady=5)

# Run GUI Loop
root.mainloop()
