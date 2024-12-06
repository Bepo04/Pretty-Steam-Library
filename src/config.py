from pathlib import Path
import json

def load_credentials():
    return load_json_file("resources/credentials.json"), load_json_file("resources/google_credentials.json")

def load_json_file(file_name):

    # Get project path
    base_dir = Path(__file__).resolve().parent.parent

    # Get file path
    filepath = base_dir / file_name

    try:
        #read file and return json content
        with filepath.open("r") as file:
            content = json.load(file)
        return content
    except FileNotFoundError:
        print(f"ERROR: File {filepath} not found, check its path")
        return None
    except json.JSONDecodeError:
        print(f"ERROR: File {filepath} has not a valid JSON format")
        return None

# check if all essential project files exist
def check_project_structure():
    # Get project path
    base_dir = Path(__file__).resolve().parent.parent

    required_files = [
        base_dir / "resources/credentials.json",
        base_dir / "resources/google_credentials.json"
    ] 

    for file in required_files:
        if not file.exists():
            return False
    return True