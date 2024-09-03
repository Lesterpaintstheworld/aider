import os
import re
import random
from pathlib import Path
from fnmatch import fnmatch

def load_ignore_patterns(ignore_file):
    if os.path.exists(ignore_file):
        with open(ignore_file, 'r') as f:
            return [line.strip() for line in f if line.strip() and not line.startswith('#')]
    return []

def is_ignored(file_path, ignore_patterns):
    for pattern in ignore_patterns:
        if pattern.endswith('/'):
            # Si le motif se termine par '/', il correspond à un répertoire
            if fnmatch(file_path, f"{pattern}*") or fnmatch(file_path, f"*/{pattern}*"):
                return True
        elif '*' in pattern:
            # Gestion des motifs avec des jokers
            if fnmatch(file_path, pattern) or fnmatch(file_path, f"*/{pattern}"):
                return True
        else:
            # Vérifier le chemin complet et le nom du fichier
            if fnmatch(file_path, pattern) or fnmatch(os.path.basename(file_path), pattern):
                return True
    return False

def is_song_related(filename):
    return re.search(r'.*song.*', filename.lower()) is not None

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
    
    gitignore_patterns = load_ignore_patterns('.gitignore')
    aiderignore_patterns = load_ignore_patterns('.aiderignore')
    ignore_patterns = gitignore_patterns + aiderignore_patterns
    
    text_files = [
        file for file in file_list 
        if is_text_file(file) 
        and not is_ignored(file, ignore_patterns)
        and not file.startswith('aider')  # Exclure les fichiers commençant par 'aider'
    ]
    
    print(f"DEBUG: Text files after applying ignore patterns: {len(text_files)}")
    
    journals_and_todolists = [file for file in text_files if is_journal_or_todolist(file, band_member)]
    discussions = [file for file in text_files if is_discussion(file)]
    concepts = [file for file in text_files if is_concept(file)]
    song_related = [file for file in text_files if is_song_related(file)]
    
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
    
    print(f"DEBUG: Song-related files: {len(song_related)}")
    print("DEBUG: Song-related files:")
    for file in song_related:
        print(f"  - {file}")
    
    relevant_files = journals_and_todolists.copy()
    
    # Add up to 2 random discussion files
    relevant_files.extend(random.sample(discussions, min(2, len(discussions))))
    
    # Add up to 4 random concept files
    relevant_files.extend(random.sample(concepts, min(4, len(concepts))))
    
    # Add up to 5 random song-related files
    relevant_files.extend(random.sample(song_related, min(5, len(song_related))))

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
    
    band_members = ["Lyra", "Rhythm", "Vox", "Pixel", "Nova"]
    for member in band_members:
        print(f"\nSelecting files for {member}:")
        selected_files = select_relevant_files(all_files, member)
        print(f"Selected files for {member}:")
        for file in selected_files:
            print(f"  - {file}")
