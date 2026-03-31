import datetime, bday_messages

today = datetime.date.today()
next_birthday = datetime.date(2027, 2, 7) # Assuming the birthday is on February 7th, 2027

days_away = next_birthday - today

if today == next_birthday:
    print(bday_messages.random_message)
else:
    print(f"Your next birthday is in {days_away.days} days!")