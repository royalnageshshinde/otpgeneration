import random
import smtplib
from email.message import EmailMessage
from email_validator import validate_email, EmailNotValidError

def generate_otp():
    """Generate a random OTP between 4 and 8 digits."""
    otp_length = random.randint(4, 8)
    return ''.join([str(random.randint(0, 9)) for _ in range(otp_length)])

def send_email(recipient_email, otp):
    """Send an email with the OTP."""
    try:
        # SMTP server details
        smtp_server = "smtp.gmail.com"
        smtp_port = 587
        sender_email = "your_email@gmail.com"
        sender_password = "your_email_password"  # Use app-specific passwords for Gmail

        # Create email message
        message = EmailMessage()
        message.set_content(f"Your one-time password is: {otp}")
        message['Subject'] = "Your OTP"
        message['From'] = sender_email
        message['To'] = recipient_email

        # Connect to SMTP server and send email
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(sender_email, sender_password)
            server.send_message(message)
        
        print("OTP sent successfully!")
    except Exception as e:
        print(f"Failed to send email: {e}")

def main():
    """Main function to validate email and send OTP."""
    recipient_email = input("Enter recipient email address: ")

    # Validate email
    try:
        valid = validate_email(recipient_email)
        recipient_email = valid.email  # Get normalized email
    except EmailNotValidError as e:
        print(f"Invalid email: {e}")
        return

    # Generate OTP and send email
    otp = generate_otp()
    print(f"Generated OTP: {otp}")  # Optional: Display OTP for debugging
    send_email(recipient_email, otp)

if __name__ == "__main__":
    main()
