import os
import re
import random

def is_journal_or_todolist(filename, band_member):
    patterns = [
        rf'.*{band_member.lower()}.*journal.*',
        rf'.*{band_member.lower()}.*todolist.*'
    ]
    return any(re.search(pattern, filename.lower()) for pattern in patterns)

def is_discussion(filename):
    return re.search(r'.*discussion.*', filename.lower()) is not None

def is_concept(filename):
    return re.search(r'.*concept.*', filename.lower()) is not None

def is_text_file(filename):
    text_extensions = ['.md', '.txt', '.py', '.js', '.html', '.css', '.json', '.yml', '.yaml', '.ini', '.cfg']
    return any(filename.lower().endswith(ext) for ext in text_extensions)

def select_relevant_files(file_list, band_member, max_files=20):
    text_files = [file for file in file_list if is_text_file(file)]
    
    journals_and_todolists = [file for file in text_files if is_journal_or_todolist(file, band_member)]
    discussions = [file for file in text_files if is_discussion(file)]
    concepts = [file for file in text_files if is_concept(file)]
    
    relevant_files = journals_and_todolists.copy()
    
    # Add up to 3 random discussion files
    relevant_files.extend(random.sample(discussions, min(3, len(discussions))))
    
    # Add up to 3 random concept files
    relevant_files.extend(random.sample(concepts, min(3, len(concepts))))

    # Add 5 other random text files
    other_files = [file for file in text_files if file not in relevant_files]
    relevant_files.extend(random.sample(other_files, min(5, len(other_files))))
    
    # Ensure we don't exceed max_files
    relevant_files = relevant_files[:max_files]
    
    return relevant_files
