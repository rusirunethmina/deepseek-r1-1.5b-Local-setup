from flask import Flask, render_template, request, jsonify
import ollama

app = Flask(__name__)

# Initialize Ollama Client
client = ollama.Client()

# Serve the UI
@app.route('/')
def index():
    return render_template('index.html')

# Handle user prompt and generate response
@app.route('/chat', methods=['POST'])
def chat():
    try:
        data = request.json
        question = data.get("prompt", "")

        if not question:
            return jsonify({"error": "Prompt is required"}), 400

        # Use Ollama to generate response
        model = "deepseek-r1:1.5b"
        response = client.generate(model=model, prompt=question)

        return jsonify({"response": response.response})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
