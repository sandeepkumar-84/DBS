import subprocess
import sys

packages = [
    "sentence-transformers",
    "faiss-cpu",
    "transformers",
    "accelerate",
    "bitsandbytes",
    "nltk",
    "bert-score",
    "tf-keras",
    "wordcloud"
]

for p in packages:
    subprocess.check_call([sys.executable, "-m", "pip", "install", p])