# Email-Sender
This project is a simple Python script for sending an email to yourself using Gmail's SMTP server.
The user enters a message, and the program sends it to the same address it uses for sending.

## 🚀 Features

* Send an email via Gmail SMTP

* User input for message text

* Secure password storage via environment variable

* Error handling for login and sending failures

## 📦 Installation and Usage
### 1. Clone the repository
`git clone https://github.com/yourusername/yourrepo.git`
`cd yourrepo`

### 2. Create an environment variable for the password

The script uses the EMAIL_PASSWORD environment variable to avoid storing the password in the code.

Linux / macOS:

`EMAIL="your_password_or_app_password"`

Windows (PowerShell):

`setx EMAIL "your_password_or_app_password"`

### 3. Set your email in the script

In the script, replace:

`sender = "your_email"`

### 4. Run the program
`python main.py`


Type your message when prompted — it will be sent to your inbox.

## ⚡ Possible Issues

* Incorrect email or App Password

* Gmail SMTP restrictions

* Missing environment variable

The script will display an error explanation if something goes wrong.
