 
from aider.utils import is_image_file

def safe_read_files(fnames):
    """
    Lit en toute sécurité le contenu des fichiers donnés.
    Retourne un dictionnaire avec les noms de fichiers comme clés et leur contenu comme valeurs.
    """
    contents = {}
    for fname in fnames:
        try:
            if is_image_file(fname):
                contents[fname] = None  # Ne pas lire les fichiers image
            else:
                with open(fname, "r", encoding="utf-8") as f:
                    contents[fname] = f.read()
        except Exception as e:
            print(f"Erreur lors de la lecture du fichier {fname}: {e}")
    return contents
from aider.utils import is_image_file

def safe_read_files(fnames):
    """
    Lit en toute sécurité le contenu des fichiers donnés.
    Retourne un dictionnaire avec les noms de fichiers comme clés et leur contenu comme valeurs.
    """
    contents = {}
    for fname in fnames:
        try:
            if is_image_file(fname):
                contents[fname] = None  # Ne pas lire les fichiers image
            else:
                with open(fname, "r", encoding="utf-8") as f:
                    contents[fname] = f.read()
        except Exception as e:
            print(f"Erreur lors de la lecture du fichier {fname}: {e}")
    return contents
