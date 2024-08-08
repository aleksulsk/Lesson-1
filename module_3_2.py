def send_email(message, recipient, *, sender="university.help@gmail.com"):
    variants = (".com", ".ru", ".net")
    if not (sender.lower().endswith(variants) and recipient.lower().endswith(variants)
            and "@" in recipient and "@" in sender):
        print("Невозможно отправить письмо с адреса", sender, "на адрес", recipient)
    elif recipient == sender:
        print("Нельзя отправить письмо самому себе!")
    elif sender == "university.help@gmail.com":
        print("Письмо успешно отправлено с адреса", sender, "на адрес", recipient)
    else:
        print("НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса ", sender, "на адрес", recipient)


send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')
