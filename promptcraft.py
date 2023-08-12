from flask import Flask, render_template, request
from models.model_handler import select_model, configure_model
from utils.prompt_generator import generate_prompt
from datetime import datetime
import socket
import json
from flask import jsonify

app = Flask(__name__)

# allowing user to select model from interface
@app.route("/get_model_config", methods=["GET"]) # route to read model_config.json & returns its contents as a JSON response onto HTML
def get_model_config():
    try:
        with open('models/model_config.json', 'r') as config_file:
            print("Reading model_config.json...")
            model_config = json.load(config_file)
            print("Model config loaded successfully:", model_config)
        return jsonify(model_config)
    except Exception as e:
        print("Error reading model_config.json:", str(e))
        return jsonify({"error": str(e)})

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        user_input = request.form["user_input"]
        user_input_model = request.form["model_select"]  # retreiving the selected model
        #selected_model = select_model()
        model_config = configure_model(user_input_model)
        generated_prompt = generate_prompt(user_input, model_config)
        
        # Get current date and time
        current_date_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        # Get system name
        system_name = socket.gethostname()
        
        return render_template("index.html", user_input=user_input, generated_prompt=generated_prompt,
                               current_date_time=current_date_time, system_name=system_name)
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
