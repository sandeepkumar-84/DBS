import json
import random
import pandas as pd
import nltk
nltk.download('punkt_tab')
from nltk import word_tokenize
from nltk.stem import PorterStemmer



def load_json_file(filename):
    with open(filename) as f:
        file = json.load(f)
    return file

filename = r'C:\AssignmentFiles\Research\intents-DBS.json'

intents = load_json_file(filename)

def create_df():
    df = pd.DataFrame({
        'Pattern' : [],
        'Tag' : []
    })

    return df

def extract_json_info(json_file, df):

    for intent in json_file['intents']:

        for pattern in intent['patterns']:

            sentence_tag = [pattern, intent['tag']]
            df.loc[len(df.index)] = sentence_tag

    return df

df = create_df()
df = extract_json_info(intents, df)
df2 = df.copy()
print(df2.shape)

############ Loaded intent JSON into df ########

stemmer = PorterStemmer()
ignore_words=['?', '!', ',', '.']

def preprocess_pattern(pattern):
    words = word_tokenize(pattern.lower())
    stemmed_words = [stemmer.stem(word) for word in words if word not in ignore_words]
    return " ".join(stemmed_words)

df['Pattern'] = df['Pattern'].apply(preprocess_pattern)

print(df.head())

print(df['Pattern'].isnull().sum())

################ Preprocessing completed

def get_corpus(series):
    words = []
    for text in series:
        for word in text.split():
            words.append(word.strip())
    return words

corpus = get_corpus(df.Pattern)

print("corpus step completed")

from collections import Counter


labels = df2['Tag'].unique().tolist()
labels = [s.strip() for s in labels]
labels

##########################
num_labels = len(labels)
id2label = {id:label for id, label in enumerate(labels)}
label2id = {label:id for id, label in enumerate(labels)}

print("Creation of lists label id2label lists Completed")

from transformers import BertForSequenceClassification, BertTokenizerFast
from transformers import AutoTokenizer, AutoModelForSequenceClassification
from transformers import pipeline
import torch
from torch.utils.data import Dataset

from transformers import AutoTokenizer, TFAutoModelForSequenceClassification
from transformers import pipeline
from transformers import DistilBertTokenizerFast
from transformers import BertForSequenceClassification, BertTokenizerFast
from transformers import TFDistilBertForSequenceClassification
from transformers import  TFTrainingArguments
#from transformers.integrations import TFTrainer
from transformers import BertTokenizer, TFBertForSequenceClassification, BertConfig
from transformers import TrainingArguments, Trainer


tokenizer_pretrained = AutoTokenizer.from_pretrained("sandeepkumar84/dbs_chat_bot_v2")
model_pretrained = AutoModelForSequenceClassification.from_pretrained("sandeepkumar84/dbs_chat_bot_v2")
print("Model loaded sucessfully")

tokenizer_pre_bert= BertTokenizerFast.from_pretrained("sandeepkumar84/dbs_chat_bot_v2")
chatbot_pre= pipeline("sentiment-analysis", model=model_pretrained, tokenizer=tokenizer_pretrained)

print("Pre bert Model loaded sucessfully")

tokenizer_pre_bert= BertTokenizerFast.from_pretrained("sandeepkumar84/dbs_chat_bot_v2")
chatbot_pre= pipeline("sentiment-analysis", model=model_pretrained, tokenizer=tokenizer_pretrained)

print("Chatbot loaded sucessfully")

def predict_from_model(text):
    
    # Change the device to "cpu" if you don't have a GPU
    device = "cuda" if torch.cuda.is_available() else "cpu"
    inputs = tokenizer_pre_bert(text, padding=True, truncation=True, max_length=512, return_tensors="pt").to(device)
    outputs = model_pretrained(**inputs)

    probs = outputs[0].softmax(1)
    pred_label_idx = probs.argmax()
    pred_label = model_pretrained.config.id2label[pred_label_idx.item()]

    return probs, pred_label_idx, pred_label

def chat_pre(chatbot):

    print("Chatbot: Hi! I am your virtual assistance,Feel free to ask, and I'll do my best to provide you with answers and assistance..")
    print("Type 'quit' to exit the chat\n\n")

    text = input("User: ").strip().lower()

    while(text != 'quit'):

        score = chatbot(text)[0]['score']
        print(score)
        if score < 0.8:
            print("Chatbot: Sorry I can't answer that\n\n")
            text = input("User: ").strip().lower()
            continue

        label = label2id[chatbot(text)[0]['label']]
        response = random.choice(intents['intents'][label]['responses'])

        print(f"Chatbot: {response}\n\n")

        text = input("User: ").strip().lower()


chat_pre(chatbot_pre)