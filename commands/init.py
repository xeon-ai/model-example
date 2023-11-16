import json
import os

def get_input(prompt: str, default=None):
    """
    Get input from the user.
    """
    if default:
        return input(f'{prompt} [{default}]: ') or default
    else:
        return input(f'{prompt}: ')
    
def get_input_boolean(prompt: str, default=None):
    """
    Gets a yes or no value from the terminal.
    """
    return get_input(prompt + ' (y/n)', default) == 'y'

def get_manifest():
    """
    Builds a new manifest.json file with the provided user inputs.
    """
    data = dict()

    # Get basic information on the project
    data['name'] = get_input('Project name')
    data['description'] = get_input('Project description')
    data['version'] = get_input('Project version', '0.0.1')
    data['author'] = get_input('Author')

    print('---')
    
    # Get specific information on the model associated with the project
    data['model'] = dict()
    data['model']['baseModel'] = get_input('Pretrained model', 'yolov8n')

    # Get information on the classes this model is trained to detect
    data['model']['classes'] = []
    while get_input_boolean('Add a class'):
        data['model']['classes'].append(get_input('Class name'))
    
    print('---')

    return data

def init(args):
    """
    Initialize a new xeon project.
    """
    # Check if we already have a manifest file
    if os.path.exists('manifest.json') and not args.force:
        print('A manifest file already exists. Use --force to overwrite it.')
        return
    
    # Get the manifest data
    manifest = get_manifest()

    # Write the manifest file
    with open('manifest.json', 'w') as f:
        json.dump(manifest, f, indent=4)
    