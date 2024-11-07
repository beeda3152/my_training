def send_email(message, recipient, *, sender = "university.help@gmail.com"):
    l = True
    if recipient == sender:
        print(f"Нельзя отправить письмо самому себе!")
        l = False
    elif "@" in recipient and "@" in sender:
        okon = [".com", ".ru", ".net"]
        for ok in okon:
            if ok in recipient and ok in sender:
                l = False
                if sender == "university.help@gmail.com":
                    print(f"Письмо успешно отправлено с адреса {sender} на адрес {recipient}")
                else:
                    print(f"НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}")
    if l:
        print(f"Невозможно отправить письмо с адреса {sender} на адрес {recipient}")

send_email("Это сообщение для проверки связи", "vasyok1337@gmail.com" )
send_email("Вы видите это сообщение как лучший студент курса!", "urban.fan@mail.com",
           sender="urban.infor@gmail.com")
send_email("Пожалуйста, исправьте задание", "urban.student@mail.ru", sender="urban.teacher@mail.uk")
send_email("Напоминаю самому себе о вебинаре", "urban.teacher@mail.ru", sender="urban.teacher@mail.ru")