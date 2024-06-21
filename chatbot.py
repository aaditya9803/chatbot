import sys
import re
from datetime import datetime

today = datetime.today()
# greet1 = ["hello", "hi", "Hey"]
# greet2 = "What would you like to have? We have "
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
foods = ["pizza", "burger", "pasta"]
menu = {
    "Monday": ["pizza", "burger"],
    "Tuesday": ["pizza", "pasta"],
    "Wednesday": ["burger", "pasta"],
    "Thursday": ["pizza", "burger", "pasta"],
    "Friday": ["pizza", "burger"],
    "Saturday": None,
    "Sunday": None,
}
prices = {
    "pizza": 10,
    "burger": 15,
    "pasta": 20,
} 


def get_chatbot_response(message):
    message = message.lower()

    if "hello" in message or "hi" in message or "hey" in message or "today" in message:
        return f"Hi,\n Today we have {', '.join(menu[days[today.weekday()]])}"
    if "tomorrow" in message:
        if today.weekday() != 6:
            tomorrow = today.weekday() + 1
        else:
            tomorrow = 0
        return f"On {days[tomorrow]}s we have {', '.join(menu[days[tomorrow]])}"
    if "yesterday" in message:
        if today.weekday() != 0:
            yesterday = today.weekday() - 1
        else:
            yesterday = 6
        return f"On {days[yesterday]}s we have {', '.join(menu[days[yesterday]])}"
    for day in days:
        if day.lower() in message:
            return f"On {day}s we have {', '.join(menu[day])}"

    for food in foods:
        if food in message.lower() and ("price" or "cost" in message.lower()):
            return f'{food} costs {prices[food]} dollars.'

    if 'menu' and ('all' or 'whole') in message.lower():
        return f"Our menu includes: {', '.join(foods)}"
    if 'menu' or ('menu' and 'today') in message.lower():
        return f"We have {', '.join(menu[days[today.weekday()]])} today."
    
    if 'hours' in message.lower():
        return 'We are open from 9 AM to 9 PM every day.'
    else:
        return 'I am sorry, I didn\'t understand that. Can you please rephrase?'

if __name__ == '__main__':
    message = sys.argv[1]
    response = get_chatbot_response(message)
    print(response)
