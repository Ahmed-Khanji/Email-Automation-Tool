import os, csv
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def store_data():
    subscribers = os.path.abspath("Subscribers")
    # go to the right directory
    directory = input("Directory of where CSV file located: ") # in my case its Downloads
    cwd = os.path.join(os.path.expanduser("~"), directory)
    os.chdir(cwd)
    print(os.getcwd())

    # Reading a csv file into dictionary
    filename = input("CSV file name: ") # in my case its emails.txt
    with open(filename) as file:
        reader = csv.DictReader(file)
        print("Data stored")
        return [row for row in reader]  # Return list of dictionaries (name and email)


def send_emails(subscribers):
    # Email server and login details
    company = input("Company name: ")
    sender_email = input("Your Outlook email: ")
    sender_password = input("Your Outlook Password: ")
    smtp_server = "smtp.office365.com"
    smtp_port = 587

    # Loop through each recipient
    for entry in subscribers:
        name = entry['name']
        email = entry['email']

        # Construct the email
        subject = f"Welcome to {company}, {name}"
        body = f"""        
Hi {name},

Welcome to {company}! We’re thrilled to have you with us.

As a valued member of our community, you’ll be the first to know about our latest updates, special offers, and exclusive content. We can't wait to help you on your journey!

If you have any questions or need assistance, feel free to reach out at any time.

Best regards,
{company}
"""

        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = email
        msg['Subject'] = subject

        msg.attach(MIMEText(body, 'plain'))

        try:
            # Set up the server and send email
            server = smtplib.SMTP(smtp_server, smtp_port)
            server.starttls()  # Secure the connection
            server.login(sender_email, sender_password)  # Log in to the email account
            text = msg.as_string()  # Convert message to string
            server.sendmail(sender_email, email, text)  # Send the email
            print(f"Email sent to {email}")
        except Exception as e:
            print(f"Failed to send email to {email}: {e}")
        finally:
            server.quit()  # Close the connection


# Retrieve data from CSV
subscribers = store_data()

# Call the function to send emails
send_emails(subscribers)