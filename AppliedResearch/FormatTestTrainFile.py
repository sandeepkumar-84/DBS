import json
import os

# Folder path
folder_path = r"C:\Research-Chatbot\DataCollection\QnA-Final"

# Input/output file name
file_name = "Test_set_v1.json"  # change if your file name is different
file_path = os.path.join(folder_path, file_name)
output_file_name = "Test_set_v2.json" 
output_file_path = os.path.join(folder_path, output_file_name)

def convert_qna_format():
    # Load existing file
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            data = json.load(f)
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return
    except json.JSONDecodeError as e:
        print(f"Error reading JSON: {e}")
        return

    # Convert only items in old format
    updated_data = []
    for item in data:
        if "question" in item and "answer" in item:
            updated_data.append({
                "query": item["question"],
                "expected_answer": item["answer"]
            })
        else:
            # Keep already converted format or unknown formats as is
            updated_data.append(item)

    # Save file back
    with open(output_file_path, "w", encoding="utf-8") as f:
        json.dump(updated_data, f, indent=2, ensure_ascii=False)

    print(f"File updated successfully: {file_path}")

if __name__ == "__main__":
    convert_qna_format()
