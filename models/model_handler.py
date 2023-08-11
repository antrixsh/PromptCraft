import json

def select_model():
    # Implement logic to let the user select a model from available options.
    return selected_model

def configure_model(selected_model):
    # Load model-specific configuration from model_config.json
    with open('models/model_config.json', 'r') as config_file:
        model_config = json.load(config_file)
    
    return model_config[selected_model]

def get_api_key(model_config):
    return model_config["api_key"]

def get_prompt_format(model_config):
    return model_config["prompt_format"]

# Other functions for model handling
