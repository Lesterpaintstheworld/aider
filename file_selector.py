import os
from aider_nova import models

import os
from pathlib import Path
from aider_nova import models
from aider_nova.utils import is_ignored_file

def select_relevant_files(all_files, max_files=20):
    """
    Utilise un modèle LLM pour sélectionner les fichiers les plus pertinents,
    en excluant les fichiers correspondant à .gitignore et .aiderignore.
    """
    model = models.Model("claude-3-haiku-20240307")  # Utiliser un modèle plus léger pour la sélection
    
    # Filtrer les fichiers ignorés
    filtered_files = [file for file in all_files if not is_ignored_file(file)]
    
    prompt = f"""Voici une liste de fichiers dans un projet. Sélectionnez les {max_files} fichiers les plus importants et pertinents pour le développement du projet, en vous concentrant sur les fichiers principaux, les concepts clés et les discussions importantes. Ignorez les fichiers de configuration, les fichiers temporaires et les fichiers moins importants. Répondez uniquement avec la liste des noms de fichiers sélectionnés, un par ligne.

Liste des fichiers :
{', '.join(filtered_files)}
"""
    
    response = model.complete(prompt)
    selected_files = response.strip().split('\n')
    
    return [file.strip() for file in selected_files if file.strip() in filtered_files]
def select_relevant_files(files):
    # Implement your file selection logic here
    # For now, let's just return all files
    return files
