try:
    import pandas as pd
    import nltk
    import transformers
    import torch
except ImportError:
    print("Required libraries not found. Installing...")
    import pip
    pip.main(['install','pandas','nltk' ,'transformers', 'torch'])


try:
    nltk.data.find('tokenizers/punkt')    
except LookupError:
    print("punkt not found. Attempting its download....")
    nltk.download('punkt')
    print("punkt has been downloaded........")


def chat_pre_response(chatbot,text):

    score = chatbot(text)[0]['score']    
    if score < 0.8:
        return "Chatbot: Sorry I can't answer that\n\n"        

    label = dbs_id_from_label[chatbot(text)[0]['label']]
    response = random.choice(intents['intents'][label]['responses'])

    return response

def provide_res_to_ui(text):
    r = chat_pre_response(chatbot_pre,text)
    return r



#print(chat_pre_response(chatbot_pre,"location"))