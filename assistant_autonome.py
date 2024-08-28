import random

class AssistantAutonome:
    def __init__(self):
        self.connaissances = {
            "salutations": ["Bonjour!", "Salut!", "Hello!"],
            "au revoir": ["Au revoir!", "À bientôt!", "Bonne journée!"]
        }

    def comprendre_commande(self, commande):
        commande = commande.lower()
        if any(mot in commande for mot in ["bonjour", "salut", "hello"]):
            return "salutations"
        elif any(mot in commande for mot in ["au revoir", "bye", "ciao"]):
            return "au revoir"
        else:
            return "inconnu"

    def generer_reponse(self, type_commande):
        if type_commande in self.connaissances:
            return random.choice(self.connaissances[type_commande])
        return "Je suis désolé, je ne comprends pas cette commande."

    def apprendre(self, commande, reponse):
        # Logique simple d'apprentissage
        mots_cles = commande.lower().split()
        if len(mots_cles) > 0:
            if mots_cles[0] not in self.connaissances:
                self.connaissances[mots_cles[0]] = []
            self.connaissances[mots_cles[0]].append(reponse)

    def executer(self, commande):
        type_commande = self.comprendre_commande(commande)
        reponse = self.generer_reponse(type_commande)
        print(reponse)
        self.apprendre(commande, reponse)

# Test de l'assistant
assistant = AssistantAutonome()
assistant.executer("Bonjour, comment ça va ?")
assistant.executer("Au revoir !")
assistant.executer("Quelle est la capitale de la France ?")
