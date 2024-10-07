from flask import Flask, request, jsonify
import openai
import os
from dotenv import load_dotenv
load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

app = Flask(__name__)

@app.route('/ask', methods=['POST'])
def ask():
    question = request.json.get('question')
    answer = get_openai_answer(question)
    return jsonify({"question": question, "answer": answer})


def get_openai_answer(question):
    # This will use the OpenAI API to fetch the answer
    response = openai.Completion.create(engine="text-davinci-003", prompt=question, max_tokens=150)
    return response.choices[0].text.strip()


if __name__ == '__main__':
    app.run(debug=True)
