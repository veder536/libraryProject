import random
import string
from django.template.loader import render_to_string
from django.core.mail import send_mail
from django.utils.html import strip_tags

# generates code for email verification
def generate_random_verification_code():
    allowed_chars = ''.join((string.ascii_letters, string.digits))
    return ''.join(random.choice(allowed_chars) for _ in range (6))

def send_verification_messsage(email, link):
    
        # html_message = f'<a href="{verification_link}">Verify</a>'

    html_message = render_to_string("base/email_verification.html", {"link": link})

    return send_mail(
        subject="Email verification code",
        message=strip_tags(html_message),
        from_email="postmaster@sandbox2930a784988743c7bc8ca3b804d5e5b6.mailgun.org",
        recipient_list=[email],
        fail_silently=False,
        html_message=html_message
    )
