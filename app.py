from flask import Flask, render_template, request, jsonify
import json
import random
from difflib import get_close_matches

app = Flask(__name__) #configures the flask application
app = Flask(__name__, static_url_path='/static') #this configures the static folder, assumes static files are in a folder called static at root level, allows for css format

# Load knowledge base from json file
def load_knowledge_base(file_path: str) -> dict:
    with open(file_path, 'r') as file:
        data: dict = json.load(file)
    return data

def save_knowledge_base(file_path: str, data: dict):
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=2)

def find_best_match(user_question: str, question: list[str]) -> str | None:
    matches: list = get_close_matches(user_question, question, n=1, cutoff=0.6)
    return matches[0] if matches else None

def get_answer_for_question(question: str, knowledge_base: dict) -> str | None:
    for q in knowledge_base["questions"]:
        if q["question"] == question:
            
            answers = q.get("answer", [])
            
            if isinstance(answers, list) and len(answers) > 1:
                return random.choice(answers)
            elif isinstance(answers, str):
                return answers
            
            
            

@app.route("/")
def index():
    return render_template("chat1.html")

@app.route("/ask", methods=["POST"])
def ask():
    user_input = request.form["user_input"]
    knowledge_base: dict = load_knowledge_base('knowledge_base.json')

    if user_input.lower() == 'quit':
        return jsonify({'bot_response': 'Goodbye!'})

    best_match: str | None = find_best_match(user_input, [q["question"] for q in knowledge_base["questions"]])
    if best_match:
        answer: str = get_answer_for_question(best_match, knowledge_base)
        print(f"Bot response: {answer}")
        return jsonify({'bot_response': answer})
    else:
        print("Bot response: I don't know the answer.")
        return jsonify({'bot_response': 'I don\'t know the answer.'})

@app.route("/train", methods=["POST"])
def train():
    training_data = request.form["training_data"]
    print(f"Received training data: {training_data}")

    knowledge_base: dict = load_knowledge_base('knowledge_base.json')

    # Assuming training_data is in the format: "question:answer"
    question, answer = training_data.split(":")
    knowledge_base["questions"].append({"question": question, "answer": answer})

    save_knowledge_base('knowledge_base.json', knowledge_base)

    return jsonify({'response': 'Training completed successfully!'})

if __name__ == "__main__":
    app.run(debug=True)