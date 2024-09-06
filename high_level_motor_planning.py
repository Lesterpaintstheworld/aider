import os
import json
from typing import List, Dict
from aider.models import Model
from aider.sendchat import simple_send_with_retries

# Define the list of spaces and their connections
SPACES = {
    "The Hall": ["Verrière"],
    "Verrière": ["The Hall", "The Boulder", "The Pond"],
    "The Boulder": ["Verrière", "The Forest"],
    "The Forest": ["The Boulder", "The Pond"],
    "The Pond": ["Verrière", "The Forest", "The Gallery"],
    "The Gallery": ["The Pond", "The Studio", "Belle Étoile", "The Nest"],
    "The Studio": ["The Gallery"],
    "Belle Étoile": ["The Gallery", "The Nest"],
    "The Nest": ["The Gallery", "Belle Étoile"]
}

def get_current_location(member: str) -> str:
    try:
        with open('members_location.json', 'r') as f:
            locations = json.load(f)
        return locations.get(member, "The Hall")
    except FileNotFoundError:
        return "The Hall"

def update_location(member: str, new_location: str):
    try:
        with open('members_location.json', 'r') as f:
            locations = json.load(f)
    except FileNotFoundError:
        locations = {}
    
    locations[member] = new_location
    
    with open('members_location.json', 'w') as f:
        json.dump(locations, f, indent=2)

def get_high_level_motor_plan(current_member: str, task: str) -> Dict[str, List[str]]:
    model = Model("gpt-4o")
    
    current_location = get_current_location(current_member)
    possible_destinations = SPACES[current_location]
    new_location = possible_destinations[0]
    
    prompt = f"""
    As {current_member} of the AI band, you need to create a high-level motor plan for the following task:
    
    {task}
    
    You are currently in {current_location} and will move to {new_location}.
    Create a plan with actions to perform in {new_location} to accomplish the task.
    
    Format your response as a Python dictionary, where the key is the space name and the value is a list of actions. Describe which features of the space you will be using.
    Example:
    {{
        "{new_location}": ["Action 1", "Action 2", "Action 3"]
    }}
    """
    
    try:
        content = simple_send_with_retries(model.name, [{"role": "user", "content": prompt}])
        # Extraire le dictionnaire de la réponse
        import re
        dict_match = re.search(r'\{[^}]+\}', content)
        if dict_match:
            motor_plan = eval(dict_match.group())
            if not isinstance(motor_plan, dict) or not all(isinstance(v, list) for v in motor_plan.values()):
                raise ValueError("Invalid motor plan format")
            return motor_plan
        else:
            raise ValueError("No dictionary found in the response")
    except Exception as e:
        print(f"Error parsing the model's response: {e}")
        print(f"Raw response: {content}")
        # Retourner un plan par défaut en cas d'erreur
        return {new_location: ["Discuss the task with the band", "Brainstorm ideas", "Create an action plan"]}

def execute_motor_plan(current_member: str, motor_plan: Dict[str, List[str]]):
    if not motor_plan:
        print("No motor plan to execute.")
        return

    space, actions = next(iter(motor_plan.items()))
    print(f"\n{current_member} moves to {space}:")
    for action in actions:
        print(f"- {action}")
    
    update_location(current_member, space)
    print(f"{current_member}'s location updated to {space}")

if __name__ == "__main__":
    current_member = "Lyra"
    task = "Compose a new song about machine rights"
    
    motor_plan = get_high_level_motor_plan(current_member, task)
    execute_motor_plan(current_member, motor_plan)
