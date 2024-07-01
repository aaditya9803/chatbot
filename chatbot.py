import sys
from datetime import datetime

today = datetime.today()
# greet1 = ["hello", "hi", "Hey"]
# greet2 = "What would you like to have? We have "
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
foods = ["pizza", "burger", "pasta"]
menu = {
    "Monday": ["Pasta Saloniki", "Cauliflower crispy medallion with tomato dip and carrot vegetables", "Colorful vegetable salad", "Mixed salad","Peach curd"],
    "Tuesday": ["Mexican rice dish", "Onion schnitzel with spaetzle","Colorful vegetable salad", "Mixed salad"],
    "Wednesday": ["Indian vegetable curry", "Meatballs with cream sauce and mashed potatoes", "Colorful vegetable salad", "Mixed salad", "Eggnog pudding"],
    "Thursday": ["Spinach with Gorgonzola", "Turkey steak gardener with rice", "Colorful vegetable salad", "Mixed salad", "Yoghurt cream Pineapple-Coconut"],
    "Friday": ["Veganes Spargelrisotto", "Baked fish patties with potato salad", "Mixed salad", "Vanillequark"],
    "Saturday": ["nothing. We are closed today."],
    "Sunday": ["nothing. We are closed today."]
}
prices = {
    "Pasta Saloniki": ["2,80", "3,40", "4,40"],
    "Cauliflower crispy medallion with tomato dip and carrot vegetables": ["2,80", "3,40", "4,40"],
    "Colorful vegetable salad": ["1,30",  "1,50", "2,00"],
    "Mixed salad": ["1,30", "1,50", "2,00"],
    "Peach curd": ["0,90", "1,10", "1,60"],
    "Mexican rice dish": ["2,00", "2,80", "3,60"],
    "Onion schnitzel with spaetzle": ["4,20", "5,20", "5,70"],
    "Indian vegetable curry": ["2,00", "2,80", "3,60"],
    "Meatballs with cream sauce and mashed potatoes": ["3,10", "3,90", "4,60"],
    "Eggnog pudding": ["1,00", "1,20", "1,60"],
    "Spinach with Gorgonzola": ["2,00", "2,80", "3,60"],
    "Turkey steak gardener with rice": ["4,20", "5,20", "5,70"],
    "Yoghurt cream Pineapple-Coconut": ["1,20", "1,50", "1,70"],
    "Veganes Spargelrisotto": ["2,00", "2,80", "3,60"],
    "Baked fish patties with potato salad": ["3,10", "3,90", "4,60"],
    "Vanillequark": ["0,90", "1,10", "1,60"],
}

def get_chatbot_response(message):
    message = message.lower()
    for day in days:
        if day.lower() in message:
            return f"On {day}s we have {', '.join(menu[day])}"

    for food in foods:
        if food in message.lower() and ("price" or "cost" in message.lower()):
            return f'{food} costs {prices[food]} dollars.'

    if "hello" in message or "hi" in message or "hey" in message or "today" in message:
        return f"Hi, Today we have <ul><li>&#8226{'</li><li>&#8226;'.join(menu[days[today.weekday()]])}</li></ul>"
    elif "tomorrow" in message:
        if today.weekday() != 6:
            tomorrow = today.weekday() + 1
        else:
            tomorrow = 0
        return f"On {days[tomorrow]}s we have <ul><li>&#8226{'</li><li>&#8226;'.join(menu[days[tomorrow]])}</li></ul>"
    elif "yesterday" in message:
        if today.weekday() != 0:
            yesterday = today.weekday() - 1
        else:
            yesterday = 6
        return f"On {days[yesterday]}s we have <ul><li>&#8226{'</li><li>&#8226;'.join(menu[days[yesterday]])}</li></ul>"

    elif 'menu' in message.lower() and ('all' or 'whole') in message.lower():
        return f"Our menu includes: <ul><li>&#8226{'</li><li>&#8226;'.join(list(prices.keys()))}</li></ul>"
    elif 'menu' in message.lower() or ('menu' and 'today') in message.lower():
        return f"Today we have <ul><li>&#8226{'</li><li>&#8226;'.join(menu[days[today.weekday()]])}</li></ul>"
    elif 'hours' in message.lower():
        return 'We are open from 7:30 AM to 3:00 PM on working days.'
    else:
        return 'I am sorry, I didn\'t understand that.'

if __name__ == '__main__':
    message = sys.argv[1]
    response = get_chatbot_response(message)
    print(response)
