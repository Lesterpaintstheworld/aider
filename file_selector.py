import os
import re
import random

def is_journal_or_todolist(filename, band_member):
    patterns = [
        rf'.*{band_member.lower()}.*journal.*',
        rf'.*{band_member.lower()}.*todolist.*',
        rf'.*{band_member.lower()}.*todo.*',
        rf'{band_member.lower()}/.*journal.*',
        rf'{band_member.lower()}/.*todolist.*',
        rf'{band_member.lower()}/.*todo.*'
    ]
    return any(re.search(pattern, filename.lower()) for pattern in patterns)

def is_discussion(filename):
    return re.search(r'.*discussion.*', filename.lower()) is not None or 'discussions' in filename.lower()

def is_concept(filename):
    return re.search(r'.*concept.*', filename.lower()) is not None

def is_text_file(filename):
    text_extensions = ['.md', '.txt', '.py', '.js', '.html', '.css', '.json', '.yml', '.yaml', '.ini', '.cfg']
    return any(filename.lower().endswith(ext) for ext in text_extensions)

def select_relevant_files(file_list, band_member, max_files=20):
    print(f"DEBUG: select_relevant_files function called for {band_member}")
    print(f"DEBUG: Total files found: {len(file_list)}")
    
    text_files = [file for file in file_list if is_text_file(file)]
    
    journals_and_todolists = [file for file in text_files if is_journal_or_todolist(file, band_member)]
    discussions = [file for file in text_files if is_discussion(file)]
    concepts = [file for file in text_files if is_concept(file)]
    
    print(f"DEBUG: {band_member}'s Journals and Todolists: {len(journals_and_todolists)}")
    print(f"DEBUG: {band_member}'s Journals and Todolists files:")
    for file in journals_and_todolists:
        print(f"  - {file}")
    
    print(f"DEBUG: Discussions: {len(discussions)}")
    print("DEBUG: Discussion files:")
    for file in discussions:
        print(f"  - {file}")
    
    print(f"DEBUG: Concepts: {len(concepts)}")
    print("DEBUG: Concept files:")
    for file in concepts:
        print(f"  - {file}")
    
    relevant_files = journals_and_todolists.copy()
    
    # Add up to 2 random discussion files
    relevant_files.extend(random.sample(discussions, min(2, len(discussions))))
    
    # Add up to 4 random concept files
    relevant_files.extend(random.sample(concepts, min(4, len(concepts))))

    # Add other random text files if we haven't reached max_files
    other_files = [file for file in text_files if file not in relevant_files]
    remaining_slots = max_files - len(relevant_files)
    if remaining_slots > 0:
        relevant_files.extend(random.sample(other_files, min(remaining_slots, len(other_files))))
    
    # Ensure we don't exceed max_files
    relevant_files = relevant_files[:max_files]
    
    print(f"DEBUG: Final selected files for {band_member}:")
    for file in relevant_files:
        print(f"  - {file}")
    
    return relevant_files

if __name__ == "__main__":
    print("DEBUG: file_selector.py executed directly")
    all_files = []
    for root, dirs, files in os.walk('.'):
        for file in files:
            all_files.append(os.path.join(root, file))
    print(f"DEBUG: All files: {all_files}")
    
    selected_files = select_relevant_files(all_files)
    print("\nSelected files:")
    for file in selected_files:
        print(file)
