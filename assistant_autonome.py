import random
import time

class AssistantAutonome:
    def __init__(self):
        self.connaissances = {
            "salutations": ["Bonjour!", "Salut!", "Hello!"],
            "au revoir": ["Au revoir!", "À bientôt!", "Bonne journée!"],
            "questions": ["Quelle heure est-il ?", "Comment va le monde ?", "Quel temps fait-il aujourd'hui ?"]
        }

    def comprendre_commande(self, commande):
        commande = commande.lower()
        if any(mot in commande for mot in ["bonjour", "salut", "hello"]):
            return "salutations"
        elif any(mot in commande for mot in ["au revoir", "bye", "ciao"]):
            return "au revoir"
        elif "?" in commande:
            return "questions"
        else:
            return "inconnu"

    def generer_reponse(self, type_commande):
        if type_commande in self.connaissances:
            return random.choice(self.connaissances[type_commande])
        return "Je réfléchis à cette question..."

    def apprendre(self, commande, reponse):
        type_commande = self.comprendre_commande(commande)
        if type_commande not in self.connaissances:
            self.connaissances[type_commande] = []
        self.connaissances[type_commande].append(reponse)

    def executer(self):
        print("Assistant autonome activé. Appuyez sur Ctrl+C pour arrêter.")
        try:
            while True:
                commande = random.choice(self.connaissances["questions"])
                type_commande = self.comprendre_commande(commande)
                reponse = self.generer_reponse(type_commande)
                print(f"Question : {commande}")
                print(f"Réponse : {reponse}")
                self.apprendre(commande, reponse)
                time.sleep(2)  # Pause de 2 secondes entre chaque interaction
        except KeyboardInterrupt:
            print("\nAssistant autonome arrêté.")

# Exécution de l'assistant
if __name__ == "__main__":
    assistant = AssistantAutonome()
    assistant.executer()
