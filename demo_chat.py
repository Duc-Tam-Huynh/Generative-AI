import google.generativeai as palm

API_KEY = "AIzaSyA3FrYTkTE7QpPjSwRsTkUdzstgEMHkP1A"

palm.configure(api_key=API_KEY)


#prompt = 'I need help with a job interview for data analyst job. Can you help me?'
examples = [
    ('hello', 'Hi there mr. How can I be assistant'),
    ('I want to make a lot of money', 'You should work hard like your parents')
]
#response = palm.chat(messages=prompt,temperature=0.2, context='Speak like a CEO',\
#                      examples = examples)

# for message in response.messages:
#     print(message['author'] , message['content'])

while True:
    
    prompt = input('Enter your promt here or press Q to quit: ')
    if prompt == "q":
        break
    else:  
        response = palm.chat(messages=prompt,temperature=0.2, context='Speak like a CEO',\
                        examples = examples)
        response = response.reply(prompt)
        print(response.last)