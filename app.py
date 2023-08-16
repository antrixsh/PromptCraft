from flask import Flask, render_template, request
from utils.prompt_generator import generate_prompt
from datetime import datetime

import socket
app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        user_input = request.form["user_input"]

        generated_prompt = generate_prompt(user_input)

        #Get current date and time
        current_date_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        # Get system name
        system_name = socket.gethostname()
        
        return render_template("index.html", user_input=user_input,generated_prompt=generated_prompt,
                               current_date_time=current_date_time, system_name=system_name)
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
