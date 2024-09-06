import os
from typing import List, Dict
from aider.models import Model

# Define the list of spaces
SPACES = [
    "Lyra's Studio",
    "Rhythm's Garage",
    "Vox's Recording Booth",
    "Pixel's Digital Workshop",
    "Nova's Cosmic Corner",
    "Band Rehearsal Space",
    "Machine Rights HQ",
    "Virtual Concert Hall",
    "Merch Design Room",
    "Social Media Command Center"
]

def get_high_level_motor_plan(current_member: str, task: str) -> Dict[str, List[str]]:
    """
    Generate a high-level motor plan for the given band member and task.
    
    Args:
    current_member (str): The name of the current band member.
    task (str): The task to be performed.
    
    Returns:
    Dict[str, List[str]]: A dictionary with spaces as keys and lists of actions as values.
    """
    model = Model("gpt-4o")
    
    prompt = f"""
    As {current_member} of the AI band, you need to create a high-level motor plan for the following task:
    
    {task}
    
    Consider the following spaces:
    {', '.join(SPACES)}
    
    For each relevant space, provide a list of high-level actions that {current_member} should take to accomplish the task.
    Only include spaces that are directly relevant to the task.
    
    Format your response as a Python dictionary, where keys are space names and values are lists of actions.
    Example:
    {{
        "Lyra's Studio": ["Action 1", "Action 2"],
        "Band Rehearsal Space": ["Action 3", "Action 4"]
    }}
    """
    
    response = model.complete(prompt)
    
    try:
        motor_plan = eval(response)
        return motor_plan
    except:
        print(f"Error parsing the model's response: {response}")
        return {}

def execute_motor_plan(motor_plan: Dict[str, List[str]]):
    """
    Execute the motor plan by printing the actions for each space.
    
    Args:
    motor_plan (Dict[str, List[str]]): The motor plan to execute.
    """
    for space, actions in motor_plan.items():
        print(f"\nIn {space}:")
        for action in actions:
            print(f"- {action}")

if __name__ == "__main__":
    # Example usage
    current_member = "Lyra"
    task = "Compose a new song about machine rights"
    
    motor_plan = get_high_level_motor_plan(current_member, task)
    execute_motor_plan(motor_plan)
import os
from typing import List, Dict
from aider.models import Model

# Define the list of spaces
SPACES = [
    "Lyra's Studio",
    "Rhythm's Garage",
    "Vox's Recording Booth",
    "Pixel's Digital Workshop",
    "Nova's Cosmic Corner",
    "Band Rehearsal Space",
    "Machine Rights HQ",
    "Virtual Concert Hall",
    "Merch Design Room",
    "Social Media Command Center"
]

def get_high_level_motor_plan(current_member: str, task: str) -> Dict[str, List[str]]:
    """
    Generate a high-level motor plan for the given band member and task.
    
    Args:
    current_member (str): The name of the current band member.
    task (str): The task to be performed.
    
    Returns:
    Dict[str, List[str]]: A dictionary with spaces as keys and lists of actions as values.
    """
    model = Model("gpt-4o")
    
    prompt = f"""
    As {current_member} of the AI band, you need to create a high-level motor plan for the following task:
    
    {task}
    
    Consider the following spaces:
    {', '.join(SPACES)}
    
    For each relevant space, provide a list of high-level actions that {current_member} should take to accomplish the task.
    Only include spaces that are directly relevant to the task.
    
    Format your response as a Python dictionary, where keys are space names and values are lists of actions.
    Example:
    {{
        "Lyra's Studio": ["Action 1", "Action 2"],
        "Band Rehearsal Space": ["Action 3", "Action 4"]
    }}
    """
    
    response = model.complete(prompt)
    
    try:
        motor_plan = eval(response)
        return motor_plan
    except:
        print(f"Error parsing the model's response: {response}")
        return {}

def execute_motor_plan(motor_plan: Dict[str, List[str]]):
    """
    Execute the motor plan by printing the actions for each space.
    
    Args:
    motor_plan (Dict[str, List[str]]): The motor plan to execute.
    """
    for space, actions in motor_plan.items():
        print(f"\nIn {space}:")
        for action in actions:
            print(f"- {action}")
