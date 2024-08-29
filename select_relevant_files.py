import os
from litellm import completion

def get_file_content(file_path, max_chars=1000):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read(max_chars)
        return content
    except Exception as e:
        return f"Error reading file: {str(e)}"

def select_relevant_files(file_list, max_files=20):
    relevant_files = []
    
    for file in file_list:
        content = get_file_content(file)
        prompt = f"Evaluate the relevance of this file for an AI music band project, focusing on the text files:\n\nFile: {file}\n\nContent:\n{content}\n\nRelevance score (0-10):"
        
        response = completion(
            model="claude-3-haiku-20240307",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=10
        )
        
        score = int(response.choices[0].message.content.strip())
        relevant_files.append((file, score))
    
    relevant_files.sort(key=lambda x: x[1], reverse=True)
    return [file for file, _ in relevant_files[:max_files]]

if __name__ == "__main__":
    all_files = [f for f in os.listdir() if os.path.isfile(f)]
    selected_files = select_relevant_files(all_files)
    print("Selected files:")
    for file in selected_files:
        print(file)
