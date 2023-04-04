from flask import Flask,request
import os
import openai

app = Flask(__name__)

openai.api_key = os.environ.get('OPENAI_KEY')


@app.route('/')
def index():
    return "<h1>Hello, World!</h1>"

@app.route('/chatgpt')
def chatgpt():
    args = request.args
    message =args.get("message")
    print(message)
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": message}]
    )
    return completion['choices'][0]['message']['content']

@app.route('/codegpt')
def codegpt():
    args = request.args
    message = args.get("message")

    # Check if the request is for generating code
    if 'language' in args and 'content' in args:
        language = args.get('language')
        content = args.get('content')
        code = generate_code_from_content(language, content)
        return code

    # If not, assume it's a chat message
    completion = openai.Completion.create(
        engine="text-davinci-002",
        prompt=message,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )
    message = completion.choices[0].text
    return message

