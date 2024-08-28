import os
from aider_nova import models

def select_relevant_files(all_files, max_files=20):
    """
    Utilise un modèle LLM pour sélectionner les fichiers les plus pertinents.
    """
    model = models.Model("claude-3-haiku-20240307")  # Utiliser un modèle plus léger pour la sélection
    
    prompt = f"""Voici une liste de fichiers dans un projet. Sélectionnez les {max_files} fichiers les plus importants et pertinents pour le développement du projet, en vous concentrant sur les fichiers principaux, les concepts clés et les discussions importantes. Ignorez les fichiers de configuration, les fichiers temporaires et les fichiers moins importants. Répondez uniquement avec la liste des noms de fichiers sélectionnés, un par ligne.

Liste des fichiers :
{', '.join(all_files)}
"""
    
    response = model.complete(prompt)
    selected_files = response.strip().split('\n')
    
    return [file.strip() for file in selected_files if file.strip() in all_files]
