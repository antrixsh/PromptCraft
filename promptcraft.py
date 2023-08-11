from models.model_handler import select_model, configure_model
from utils.prompt_generator import generate_prompt

def main():
    print("Welcome to PromptCraft!")
    
    user_input = input("Enter your question or prompt: ")
    selected_model = select_model()
    model_config = configure_model(selected_model)
    
    generated_prompt = generate_prompt(user_input, model_config)
    
    print("Generated Prompt:")
    print(generated_prompt)
    
if __name__ == "__main__":
    main()
