import os
import spacy
import json
from transformers import T5Tokenizer, AutoModelForSeq2SeqLM

# Load spaCy NER model (English)
nlp = spacy.load("en_core_web_sm")


print("Loading spaCy model for NER...")


print("Loading transformers for question generation...")
# Load QG model and tokenizer
tokenizer = T5Tokenizer.from_pretrained("valhalla/t5-base-qg-hl")

print
model = AutoModelForSeq2SeqLM.from_pretrained("valhalla/t5-base-qg-hl")

print("Loading QG model and tokenizer...")

def generate_question(context, answer):
    # Highlight answer in context as required by model
    highlighted_context = context.replace(answer, f"<hl> {answer} <hl>")
    inputs = tokenizer.encode(highlighted_context, return_tensors="pt")
    outputs = model.generate(inputs)
    question = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return question

def extract_answer_candidates(text):
    doc = nlp(text)
    # Extract named entities as potential answers
    return list(set(ent.text for ent in doc.ents))

# Assuming corpus is loaded from your snippet:
corpus = []
folder_path = "C:/Research-Chatbot/DataCollection/GeneratQnA"

print(f"Loading files from: {folder_path}")
if not os.path.exists(folder_path):
    print(f"Folder {folder_path} does not exist.")
    exit(1)


for file_name in os.listdir(folder_path):
    file_path = os.path.join(folder_path, file_name)
    print(f"Loading file: {file_path}")
    try:
        with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
            corpus.extend([para.strip() for para in content.split('\n') if len(para.strip()) > 10])
    except Exception as e:
        print(f"Error reading {file_path}: {e}")

print(f"Loaded {len(corpus)} paragraphs.")

# Generate QA pairs for first N paragraphs (to keep it small here)
N = len(corpus)
qa_pairs_raw = []

for i, paragraph in enumerate(corpus[:N]):
   # print(f"\nParagraph {i+1}: {paragraph}")
    answers = extract_answer_candidates(paragraph)
    if not answers:
        print("No answer candidates found.")
        continue
    
    for answer in answers:
        try:
            question = generate_question(paragraph, answer)
            qa_pairs_raw.append({'question': question, 'answer': answer, 'context': paragraph}) 
           # print(f"Q: {question}\nA: {answer}")
        except Exception as e:
            print(f"Error generating question for answer '{answer}': {e}")

# qa_pairs_raw now contains generated question-answer-context triples


output_path = "C:/Research-Chatbot/DataCollection/GeneratedQnA/qa_pairs_raw.json"
with open(output_path, 'w', encoding='utf-8') as f:
    json.dump(qa_pairs_raw, f, ensure_ascii=False, indent=2)

print(f"\nSaved {len(qa_pairs_raw)} QA pairs to: {output_path}")


