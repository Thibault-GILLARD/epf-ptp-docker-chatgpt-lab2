from flask import Flask,request
import os
import openai

app = Flask(__name__)

openai.api_key = os.environ.get('OPENAI_KEY')

# Function to generate code from content
def generate_code_from_content(language, content):
    # Code generation logic goes here
    code = f"{language} code generated from content: {content}"
    return code

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


@app.route('/generate_code')
def generate_code():
    args = request.args
    if 'language' in args and 'content' in args:
        language = args.get('language')
        content = args.get('content')
        code = generate_code_from_content(language, content)
        return code
    else:
        return "Please provide both 'language' and 'content' parameters to generate code."

