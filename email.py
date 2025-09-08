from django.core.mail import send_mail

def send_invite_email(subject, message, recipient):
    send_mail(subject, message, 'noreply@eventr.com', [recipient])
