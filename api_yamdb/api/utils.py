import random

from django.core.mail import send_mail

CODE_LEN = 5

def send_confirmation_code(email, confirmation_code):
    send_mail(
        subject='Код подтверждения',
        message=f'Ваш код: {confirmation_code}',
        from_email='info@api_yamdb.ru',
        recipient_list=[email],
    )


def generate_confirmation_code():
    digs = '1234567890'
    code = ''
    for _ in range(CODE_LEN):
        code += random.choice(digs)
    return code
