# Email-Sender
This project is a simple Python script for sending an email to yourself using Gmail's SMTP server.
The user enters a message, and the program sends it to the same address it uses for sending.

##🚀 Features

* Send an email via Gmail SMTP

* User input for message text

* Secure password storage via environment variable

* Error handling for login and sending failures

📦 Installation and Usage
1. Clone the repository
git clone https://github.com/yourusername/yourrepo.git
cd yourrepo

2. Install dependencies

The script uses only the Python standard library — no additional packages required.

3. Create an environment variable for the password

The script uses the EMAIL_PASSWORD environment variable to avoid storing the password in the code.

Linux / macOS:
export EMAIL_PASSWORD="your_password_or_app_password"

Windows (PowerShell):
setx EMAIL_PASSWORD "your_password_or_app_password"


⚠️ Important:
Gmail no longer supports “less secure apps”.
You must use a Google App Password:
Google Account → Security → App passwords.

4. Set your email in the script

In the script, replace:

sender = "your_email"


with your real Gmail address:

sender = "your_email@gmail.com"

5. Run the program
python main.py


Type your message when prompted — it will be sent to your inbox.

🛠 Example
Type your message: Hello from Python!
The message was sent successfully!

⚡ Possible Issues

Incorrect email or App Password

Gmail SMTP restrictions

Missing environment variable

The script will display an error explanation if something goes wrong.
