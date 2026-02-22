from flask import Flask, render_template, request
from openai import OpenAI

app = Flask(__name__)

# Replace with your API key
client = OpenAI(api_key="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")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get", methods=["POST"])
def chatbot_response():
    user_message = request.form["msg"]

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "user", "content": user_message}
        ]
    )

    return response.choices[0].message.content

if __name__ == "__main__":
    app.run(debug=True)