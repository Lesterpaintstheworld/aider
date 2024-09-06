import os
from openai import OpenAI
from dotenv import load_dotenv

# Charger les variables d'environnement depuis le fichier .env
load_dotenv()

def generate_image(prompt, output_path):
    client = OpenAI()
    
    response = client.images.generate(
        model="dall-e-3",
        prompt=prompt,
        size="1024x1024",
        quality="standard",
        n=1,
    )
    
    image_url = response.data[0].url
    
    # Télécharger et sauvegarder l'image
    import requests
    img_data = requests.get(image_url).content
    with open(output_path, 'wb') as handler:
        handler.write(img_data)

def process_file(file_path):
    base_name = os.path.splitext(os.path.basename(file_path))[0]
    image_count = 1
    
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            if "--ar" in line:
                prompt = line.strip().replace('"', '')
                output_path = f"images/{base_name}_{image_count}.png"
                
                generate_image(prompt, output_path)
                print(f"Image générée : {output_path}")
                
                image_count += 1

if __name__ == "__main__":
    input_file = "concepts/voices_of_the_circuits.md"
    
    # Créer le dossier 'images' s'il n'existe pas
    os.makedirs("images", exist_ok=True)
    
    process_file(input_file)