import json
import os

# Paths
input_path = r"C:\Research-Chatbot\DataCollection\QnA-Final\Training_set_v1.json"
output_path = r"C:\Research-Chatbot\DataCollection\QnA-Final\Training_set_v1_paraghraph.txt"

def convert_json_to_text(input_file, output_file):
    if not os.path.exists(input_file):
        raise FileNotFoundError(f"The file {input_file} does not exist.")

    with open(input_file, "r", encoding="utf-8") as f:
        data = json.load(f)

    paragraphs = []
    for item in data:
        question = item.get("question", "").strip()
        answer = item.get("answer", "").strip()
        context = item.get("context", "").strip()

        # Merge into one paragraph
        paragraph = f"{question} {answer} {context}".strip()
        paragraphs.append(paragraph)

    # Write paragraphs to output file
    with open(output_file, "w", encoding="utf-8") as f:
        for para in paragraphs:
            f.write(para + "\n")

    print(f"Converted {len(paragraphs)} entries into paragraphs.")
    print(f"Saved to: {output_file}")

if __name__ == "__main__":
    convert_json_to_text(input_path, output_path)
