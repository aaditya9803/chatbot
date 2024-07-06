import sys
from datetime import datetime
import json

today = datetime.today()
# greet1 = ["hello", "hi", "Hey"]
# greet2 = "What would you like to have? We have "
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
menu = {
    "Monday": ["Pasta Saloniki", "Cauliflower crispy medallion with tomato dip and carrot vegetables", "Colorful vegetable salad", "Mixed salad","Peach curd"],
    "Tuesday": ["Mexican rice dish", "Onion schnitzel with spaetzle","Colorful vegetable salad", "Mixed salad"],
    "Wednesday": ["Indian vegetable curry", "Meatballs with cream sauce and mashed potatoes", "Colorful vegetable salad", "Mixed salad", "Eggnog pudding"],
    "Thursday": ["Spinach with Gorgonzola", "Turkey steak gardener with rice", "Colorful vegetable salad", "Mixed salad", "Yoghurt cream Pineapple-Coconut"],
    "Friday": ["Veganes Spargelrisotto", "Baked fish patties with potato salad", "Mixed salad", "Vanillequark"],
    "Saturday": ["nothing. We are closed."],
    "Sunday": ["nothing. We are closed."]
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

def get_chatbot_response(message, state):
    message = message.lower()
    response = {}
    # for day in days:
    #     if day.lower() in message:
    #         return f"On {day}s we have <ol><li>{'</li><li>'.join(menu[day])}</li></ol>"

    # for food in foods:
    #     if food in message.lower() and ("price" or "cost" in message.lower()):
    #         return f'{food} costs {prices[food]} dollars.'
        

    if 'hi' in message.lower() or 'hello' in message.lower() or 'hey' in message.lower() or 'today' in message.lower():
        response['message'] = "Hi, Would you like to know the menu for today?"
        response['state'] = {'lastMessage': 'menu_today'}

    elif state['lastMessage'] == 'menu_today':
        if 'yes' in message.lower() or 'yeah' in message.lower() or 'sure'in message.lower() or 'ok'in message.lower() or 'okay'in message.lower() or 'today' in message.lower():
            response['message'] = f"Hi, Today we have <ol><li>{'</li><li>'.join(menu[days[today.weekday()]])}</li></ol>"
            response['state'] = {'lastMessage': 'food_list'}
        if 'No' in message.lower() or 'no' in message.lower() or 'nope'in message.lower():
            response['message'] = "Say 'hi' to start again."
            response['state'] = {'lastMessage': None}
        else:
            response['message'] = "I could not understand you. <br> Say 'hi' to start again."
            response['state'] = {'lastMessage': None}

    elif "tomorrow" in message:
        if today.weekday() != 6:
            tomorrow = today.weekday() + 1
        else:
            tomorrow = 0
        response['message'] = f"On {days[tomorrow]}s we have <ol><li>{'</li><li>'.join(menu[days[tomorrow]])}</li></ol>"
        response['state'] = {'lastMessage': 'menu_tomorrow'}

    elif state['lastMessage'] == 'menu_tomorrow':
        if 'order' in message.lower() or 'order food' in message.lower() or 'pack'in message.lower() or 'ok'in message.lower() or 'okay'in message.lower() or 'today' in message.lower():
            response['message'] = "You can't order food for tomorrow. <br> Please comeback tomorrow to order <br> Thank you!"
            response['state'] = {'lastMessage': None}

        # else:
        #     response['message'] = "I could not understand you. <br> Say 'hi' to start again."
        #     response['state'] = {'lastMessage': None}
        
    elif "yesterday" in message:
        if today.weekday() != 0:
            yesterday = today.weekday() - 1
        else:
            yesterday = 6
        response['message'] = f"On {days[tomorrow]}s we have <ol><li>{'</li><li>'.join(menu[days[yesterday]])}</li></ol>"
        response['state'] = {'lastMessage': 'menu_yesterday'} 

    # elif state['lastMessage'] == 'food_list':
    #     if message in prices.keys():
    #         response['message'] = f'{message} costs {", ".join(prices[message])} euros.'
    #         response['state'] = {'lastMessage': 'price'}
    #     else:
    #         response['message'] = "Sorry, I don't have the price for that. Would you like to know the menu for tomorrow?"
    #         response['state'] = {'lastMessage': 'menu_tomorrow'}




    # elif "tomorrow" in message:
    #     if today.weekday() != 6:
    #         tomorrow = today.weekday() + 1
    #     else:
    #         tomorrow = 0
    #     return f"On {days[tomorrow]}s we have <ol><li>{'</li><li>'.join(menu[days[tomorrow]])}</li></ol>"
    # elif "yesterday" in message:
    #     if today.weekday() != 0:
    #         yesterday = today.weekday() - 1
    #     else:
    #         yesterday = 6
    #     return f"On {days[yesterday]}s we have <ol><li>{'</li><li>'.join(menu[days[yesterday]])}</li></ol>"

    elif 'menu' in message.lower() and ('all' or 'whole') in message.lower():
        return f"Our menu includes: <ol><li>{'</li><li>'.join(list(prices.keys()))}</li></ol>"
    elif 'menu' in message.lower() or ('menu' and 'today') in message.lower():
        return f"Today we have <ol><li>{'</li><li>'.join(menu[days[today.weekday()]])}</li></ol>"
    elif 'hours' in message.lower():
        return 'We are open from 7:30 AM to 3:00 PM on working days.'
    elif 'thank you' in message.lower() or 'thankyou' in message.lower():
        return 'You are welcome! Have a nice day! <br> Bye!'
    else:
        response['message'] = "Please say 'hi' to start again."
        response['state'] = {'lastMessage': None}
    return response

if __name__ == '__main__':
    message = sys.argv[1]
    state = json.loads(sys.argv[2])
    response = get_chatbot_response(message, state)
    print(json.dumps(response))
