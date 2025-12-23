import random
print("Hi! I am your simple Rule-Based Chatbot")
print("Type 'bye' to exit\n")
#Predefined replies stored in list
hello_responses=["Hello!","Hey there!","Hey,how can I help you?","Greetings!"]
bye_responsese=["GodBye!","See you later!","Bye! take care!","Farewell!","Have a good day, Sir!"]
thanks_responses=["You're welcome!","No problem!","Glad to Help!","Anytime!","No issue!"]
Unknown_responses=["I am not sure about that.","Could you repeat that please?",
                  "Interesting...Tell me more!","Hmm...I don't Undertand."]
while True:
    user_input=input("Enter Something to chat with me:").lower()#convert to lowercase for easy matching.
    #conditions to check keywords
    if "hello" in user_input or "hi" in user_input:
        print("Bot:",random.choice(hello_responses))
    elif "bye" in user_input:
        print("Bot:",random.choice(bye_responsese))
        break
    elif "thanks" in user_input or "thank you" in user_input:
        print("Bot:",random.choice(thanks_responses))
    else:
        print("Bot:",random.choice(Unknown_responses))
