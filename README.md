# 🌐 Website Status Checker

A GUI-based Python tool that checks if websites are **online or offline**.  
It allows users to enter multiple website URLs, displays their status, and logs the results.  
If a website is **down**, it sends an **email notification**. 🚀  

---

## 🔥 Features  
✅ **Check Multiple Websites** - Enter multiple URLs and check their status at once.  
✅ **GUI Interface** - Simple & user-friendly **Tkinter-based GUI**.  
✅ **Error Handling** - Detects **timeouts, connection errors, and invalid URLs**.  
✅ **Email Notifications** - Sends an **alert** if a website is **offline**.  
✅ **Logging** - Saves website status updates to a log file (`website_status.log`).  

---

## 📂 Installation  

### 🔹 **Step 1: Clone the Repository**
```sh
git clone https://github.com/Burhanali2211/WebsiteStatusChecker.git
cd WebsiteStatusChecker
```
### 🔹 Step 2: Install Dependencies
Make sure you have Python installed (≥ 3.7). Install the required libraries:
```bash
pip install requests smtplib
```
## 🚀 Usage
### 🔹 Run the Application
python website_checker.py
🔹 How to Use
```bash
1️⃣ Enter one or multiple website URLs (one per line).
2️⃣ Click "Check Status".
3️⃣ See the results (✅ Online, ❌ Offline, ⚠️ Slow Response).
4️⃣ If a website is down, an email alert is sent.
5️⃣ Logs are stored in website_status.log.
```


## 🛠️ Configuration
🔹 Email Notifications (Optional)
To enable email alerts for offline websites:
1️⃣ Open website_checker.py.
2️⃣ Replace these with your email credentials:

```bash
EMAIL_SENDER = "your_email@gmail.com"
EMAIL_PASSWORD = "your_app_password"
EMAIL_RECEIVER = "receiver_email@gmail.com"
```
3️⃣ Enable Less Secure Apps (if using Gmail) or use an App Password.
