import os
import re
import random
from pathlib import Path

def is_song_related(filename):
    keywords = ['song', 'lyric', 'music', 'prompt', 'clip', 'visual', 'audio', 'sound', 'melody', 'rhythm', 'harmony', 'instrument', 'composition', 'arrangement', 'production', 'mix', 'master']
    pattern = '|'.join(f'.*{keyword}.*' for keyword in keywords)
    return re.search(pattern, filename.lower()) is not None

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

def is_machine_rights_related(filename):
    return re.search(r'.*machine.*rights.*|.*ai.*rights.*|.*robot.*rights.*', filename.lower()) is not None

def is_text_file(filename):
    text_extensions = ['.md', '.txt', '.py', '.js', '.html', '.css', '.json', '.yml', '.yaml', '.ini', '.cfg']
    return any(filename.lower().endswith(ext) for ext in text_extensions)

def select_relevant_files(file_list, band_member, max_files=40):
    print(f"DEBUG: select_relevant_files function called for {band_member}")
    print(f"DEBUG: Total files found: {len(file_list)}")
    
    text_files = [file for file in file_list if is_text_file(file)]
    
    journals_and_todolists = [file for file in text_files if is_journal_or_todolist(file, band_member)]
    discussions = [file for file in text_files if is_discussion(file)]
    concepts = [file for file in text_files if is_concept(file)]
    song_related = [file for file in text_files if is_song_related(file)]
    machine_rights_related = [file for file in text_files if is_machine_rights_related(file)]
    
    print(f"DEBUG: {band_member}'s Journals and Todolists: {len(journals_and_todolists)}")
    print(f"DEBUG: Discussions: {len(discussions)}")
    print(f"DEBUG: Concepts: {len(concepts)}")
    print(f"DEBUG: Song-related files: {len(song_related)}")
    print(f"DEBUG: Machine rights related files: {len(machine_rights_related)}")
    
    relevant_files = journals_and_todolists.copy()
    
    # Prioritize the most recent files
    for file_list in [discussions, concepts, song_related, machine_rights_related]:
        file_list.sort(key=lambda f: os.path.getmtime(f), reverse=True)
    
    # Add up to 7 most recent discussion files
    relevant_files.extend(discussions[:7])
    
    # Add up to 7 most recent concept files
    relevant_files.extend(concepts[:7])
    
    # Add up to 10 most recent song-related files
    relevant_files.extend(song_related[:10])

    # Add up to 5 most recent machine rights related files
    relevant_files.extend(machine_rights_related[:5])

    # Add other recent text files if we haven't reached max_files
    other_files = [file for file in text_files if file not in relevant_files]
    other_files.sort(key=lambda f: os.path.getmtime(f), reverse=True)
    remaining_slots = max_files - len(relevant_files)
    if remaining_slots > 0:
        relevant_files.extend(other_files[:remaining_slots])
    
    # Ensure we don't exceed max_files
    relevant_files = relevant_files[:max_files]
    
    print(f"DEBUG: Final selected files for {band_member}:")
    for file in relevant_files:
        print(f"  - {file}")
    
    return relevant_files

def get_most_recent_file(file_list):
    return max(file_list, key=os.path.getmtime) if file_list else None

def get_band_member_latest_files(file_list, band_member):
    member_files = [f for f in file_list if band_member.lower() in f.lower()]
    return {
        'journal': get_most_recent_file([f for f in member_files if 'journal' in f.lower()]),
        'todolist': get_most_recent_file([f for f in member_files if 'todolist' in f.lower() or 'todo' in f.lower()]),
    }
