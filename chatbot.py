import sys
from datetime import datetime
import json

today = datetime.today()

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
# Students / Staff / Guests
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
foods = list(prices.keys())

def get_chatbot_response(message, state):
    message = message.lower()
    if message == "yes":
        message = "yes_"
    if message == "no":
        message = "no_"
    response = {}
    available_days = []
        

    if 'hi' in message or 'hello' in message or 'hey' in message or 'today' in message or 'start' in message:
        response['message'] = "Hi, Would you like to know the menu for today?"
        response['state'] = {'lastMessage': 'menu_today'}

    elif state['lastMessage'] == 'menu_today':
        if 'yes_' in message or 'yeah' in message or 'sure'in message or 'ok'in message or 'okay'in message or 'today' in message:
            response['message'] = f"Hi, Today we have <ol><li>{'</li><li>'.join(menu[days[today.weekday()]])}</li></ol> <br> Which food would you like to know about or order?"
            response['state'] = {'lastMessage': 'know_about'}
        elif 'no_' in message or 'nope'in message:
            response['message'] = "Say 'hi' to start again."
            response['state'] = {'lastMessage': None}
        elif 'tomorrow' in message or ('tomorrow' in message and 'no' in message):
            response['message'] = f"Would you like to know the menu for tomorrow?"
            response['state'] = {'lastMessage': 'menu_tomorrow'}
        elif 'yesterday' in message or ('yesterday' in message and 'no' in message):
            response['message'] = f"Would you like to know the menu for yesterday?"
            response['state'] = {'lastMessage': 'menu_yesterday'}

        elif any(day.lower() in message for day in days):
            day_mentioned = next(day for day in days if day.lower() in message)
            response['message'] = f"On {day_mentioned}s we have <ol><li>{'</li><li>'.join(menu[day_mentioned])}</li></ol>"
            response['state'] = {'lastMessage': None}
        
        elif any(food.lower() in message for food in foods):
            food_mentioned = next(food for food in foods if food.lower() in message)
            for day in days:
                if food_mentioned in menu[day]:
                    available_days.append(day)
                    response['message'] = f"The food is available on <ul><li>{'</li><li>'.join(available_days)}s</li><br>It costs:<ul><li>{prices[food_mentioned][0]} euros for students,</li><li>{prices[food_mentioned][1]} euros for staff,</li><li>{prices[food_mentioned][2]} euros for guests.</li></ul>"
                    response['state'] = {'lastMessage': None}

        elif 'hours' in message:
            response['message'] = f"We are open from 7:30 AM to 3:00 PM on working days."
            response['state'] = {'lastMessage': None}
        
        elif 'menu' in message and ('all' in message or 'whole'in message):
            response['message'] = f"Our menu includes: <ol><li>{'</li><li>'.join(list(prices.keys()))}</li></ol>"
            response['state'] = {'lastMessage': None}
    
        else:
            response['message'] = "I could not understand you. <br> Say 'hi' to start again."
            response['state'] = {'lastMessage': None}


    elif state['lastMessage'] == 'menu_tomorrow' or 'tomorrow' in message:
        if today.weekday() != 6:
            tomorrow = today.weekday() + 1
        else:
            tomorrow = 0
        if 'yes_' in message or 'yeah' in message or 'right'in message:
            response['message'] = f"On {days[tomorrow]}s we have <ol><li>{'</li><li>'.join(menu[days[tomorrow]])}</li></ol>"
            response['state'] = {'lastMessage': 'menu_tomorrow'}
        
        elif 'order' in message or 'order food' in message or 'pack'in message or '1'in message or '2'in message or '3' in message or '4' in message or '5' in message:
            response['message'] = "You can't order food for tomorrow. <br> Please comeback tomorrow to order <br> Thank you!"
            response['state'] = {'lastMessage': None}
        else:
            response['message'] = "Say 'hi' to start again."
            response['state'] = {'lastMessage': None}



    elif state['lastMessage'] == 'menu_yesterday' or 'yesterday' in message:
        if today.weekday() != 0:
            yesterday = today.weekday() - 1
        else:
            yesterday = 6
        if 'yes_' in message or 'yeah' in message or 'right'in message:
            response['message'] = f"On {days[yesterday]}s we have <ol><li>{'</li><li>'.join(menu[days[yesterday]])}</li></ol>"
            response['state'] = {'lastMessage': 'menu_yesterday'} 
        
        elif 'order' in message or 'order food' in message or 'pack'in message or '1'in message or '2'in message or '3' in message or '4' in message or '5' in message:
            response['message'] = "You can't order food for Yesterday. <br> But Hey!! You can order for today. <br> Would you like to know the menu for today?"
            response['state'] = {'lastMessage': 'menu_today'}
        else:
            response['message'] = "Say 'hi' to start again."
            response['state'] = {'lastMessage': None}

    elif state['lastMessage'] == 'know_about':
        valid_selection = False
        for i in range(len(menu[days[today.weekday()]])):
            if f"{i+1}" in message:
                response['message'] = f"{menu[days[today.weekday()]][i]} costs:<ul><li>{prices[menu[days[today.weekday()]][i]][0]} euros for students,</li><li>{prices[menu[days[today.weekday()]][i]][1]} euros for staff,</li><li>{prices[menu[days[today.weekday()]][i]][2]} euros for guests.</li></ul><br> So, what type of customer are you?"
                response['state'] = {'lastMessage': 'user_type'}
                valid_selection = True
                break
        if not valid_selection:
            response['message'] = "Invalid selection. Say 'hi' to start again."
            response['state'] = {'lastMessage': None}


    elif state['lastMessage'] == 'user_type':
        for i in range(0, len(menu[days[today.weekday()]])):
            if 'student' in message or '1' in message:
                response['message'] = f"It will be {prices[menu[days[today.weekday()]][i]][0]} euro. <br> Do you confirm your Order?"
                response['state'] = {'lastMessage': 'confirm_order'}
            elif 'staff' in message or '2' in message:
                response['message'] = f"It will be {prices[menu[days[today.weekday()]][i]][1]} euro. <br> Do you confirm your Order?"
                response['state'] = {'lastMessage': 'confirm_order'}
            elif 'guest' in message or '3' in message:
                response['message'] = f"It will be {prices[menu[days[today.weekday()]][i]][2]} euro. <br> Do you confirm your Order?"
                response['state'] = {'lastMessage': 'confirm_order'}
            else:
                response['message'] = "Say 'hi' to start again."
                response['state'] = {'lastMessage': None}

    elif state['lastMessage'] == 'confirm_order':
        if 'yes_' in message:
            response['message'] = "Thank you for ordering.<br> Please pay at the counter. <br> Have a nice day!"
            response['state'] = {'lastMessage': None}
        elif 'no_' in message:
            response['message'] = "Your order has been canceled. <br> Say 'hi' to start again."
            response['state'] = {'lastMessage': None}



    elif 'thank you' in message or 'thankyou' in message or 'thanks' in message:
        response['message'] = "You are welcome! Have a nice day! <br> Bye!"
        response['state'] = {'lastMessage': None}
    else:
        response['message'] = "Please say 'hi' to start again."
        response['state'] = {'lastMessage': None}
    return response

if __name__ == '__main__':
    message = sys.argv[1]
    state = json.loads(sys.argv[2])
    response = get_chatbot_response(message, state)
    print(json.dumps(response))
