"""
    Файл, который предназначен для парсинга входящих писем с почты Яндекса
    Возвращает список словарей. В словаре 4 поля: 
    subject - тема письма, text - текст письма, username - имя отправителя, 
    email - email отправителя
"""

import email
import imaplib
from email.header import decode_header


def read_incoming_emails(email_user, email_pass):
    """
        Функция возвращает список словарей. В словаре 4 поля: 'subject', 'username', 'email', 'text'
        В списке содержатся все письма, которые были получены во время работы функции
        Функция вызывается раз в 10 секунд
    """
    mail = imaplib.IMAP4_SSL('imap.yandex.ru')
    try:
        mail.login(email_user, email_pass)
    except imaplib.IMAP4.error:
        return ('Ошибка авторизации')
    # Папка "Входящие"
    mail.select('inbox')

    response_data = []

    messages = mail.search(None, 'UNSEEN')[1]
    for num in messages[0].split():

        message_info = {}

        data = mail.fetch(num, '(RFC822)')[1]
        email_msg = data[0][1]
        msg = email.message_from_bytes(email_msg)

        # Получение темы сообщения
        subject = decode_header(msg["Subject"])[0][0]
        if isinstance(subject, bytes):
            subject = subject.decode()
        # Получение отправителя сообщения
        from_ = msg.get("From").split('<')

        message_info['subject'] = subject
        message_info['username'] = from_[0].strip()
        message_info['email'] = from_[1].replace('>', '').strip('\r\n')

        # Если сообщение многочастное, получаем тело сообщения
        if msg.is_multipart():
            for part in msg.walk():
                if part.get_content_type() == "text/plain":
                    body = part.get_payload(decode=True).decode()
                    try:
                        if 'text' not in message_info.keys():
                            message_info['text'] = body
                        else:
                            raise ValueError('Сообщение содержит несколько текстовых частей')
                        break
                    except ValueError as e:
                        print(e)
        else:
            print('Сообщение не удалось декодировать')
        response_data.append(message_info)
    mail.logout()
    if response_data:
        return response_data
    else:
        return ('Новых писем нет')