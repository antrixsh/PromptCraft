# PromptCraft
Crafting OpenAI Prompts from Human Language

PromptCraft: Convert Human English Language into OpenAI Prompts

##### Welcome to PromptCraft, a Python-based open-source tool that enables seamless conversion of human-written English language into prompts suitable for OpenAI models. With PromptCraft, you can effortlessly bridge the gap between human communication and machine-generated responses using the power of OpenAI's language models.
A Proof of Concept Software that uses OpenAI API itself to improve the performance of a Task requested in input for a hypothetical Agent.
In my view an initial expansion of the prompt should be the first task an Agent should perform. Optimizing the initial prompt (with something Grammarly-like) could also help generate a better response. In addition to this, an Agent should extract as much information as possible from the input task such as: geographical locations, ISO 639-1 language codes, URLs, etc. for possible later use.

Also work as a  prompt defence is a multi-layer defence that can be used to protect your applications against prompt injection attacks. You can use this with any LLM APIs (whether Gemini Ai, Bard, LlaMa, ChatGPT - or any other LLM) These types of attack are complex, and are difficult to solve with a single layer of defence.

### Key Features

    - User-Friendly Interface: PromptCraft offers a user-friendly interface that allows users to input questions, statements, or prompts in plain English, which are then transformed into suitable prompts for OpenAI models.

    - Automatic Prompt Generation: Our tool automatically generates prompts that adhere to the requirements of different OpenAI models, ensuring optimal results without the need for manual prompt crafting.

    - Customization Options: PromptCraft lets you customize the generated prompts based on your preferred model, response length, and other relevant parameters. This flexibility ensures that the generated responses meet your specific needs.

    - Open Source: PromptCraft is open-source and actively maintained by a community of developers. Feel free to contribute, suggest improvements, and customize the tool according to your requirements.
    - Rate your prompts by quality (prompt efficiency score), API to import and export categories and prompts also Support for managing multiple types of prompts (Gemini AI, Gemma, ChatGPT, Stable Diffusion, Custom prompts)
    - a prompt shield is made up of multiple ' rings' of defence.


### Installation

To get started with PromptCraft, follow these steps:

    Clone the repository:
    git clone https://github.com/yourusername/promptcraft.git
cd promptcraft
### Install the required dependencies:
pip install -r requirements.txt

### Run the tool:
python promptcraft.py
## Usage

    - Launch the PromptCraft tool by executing python promptcraft.py in your terminal.

    - Input your question, statement, or prompt in English when prompted.

    - Choose your preferred Gemini Ai or OpenAI model and set other customization options if desired.

    - The tool will generate the appropriate prompt for the chosen model and display the results.

    - Copy the generated prompt and use it to interact with Gemini AI or OpenAI's API for responses.

### Contributing

We welcome contributions from the community to make PromptCraft even better. If you have ideas for improvements, bug fixes, or new features, please follow these steps:

    - Fork the repository.

    - Create a new branch for your feature or fix.

    - Make your changes and test thoroughly.

    - Submit a pull request, explaining your changes and their benefits.

### License

PromptCraft is released under the MIT License.
### Contact

If you have any questions, suggestions, or feedback, feel free to reach out to us at antrixsh@gmail.com or open an issue on the GitHub repository.

Get ready to unlock the potential of human-AI interaction with PromptCraft. Craft prompts seamlessly and explore the capabilities of OpenAI models like never before!
