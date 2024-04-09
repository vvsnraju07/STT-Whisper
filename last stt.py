import whisper 
from flask import Flask, render_template, request

app = Flask(__name__)

def runSTT(file_path):
    model = whisper.load_model("base")
    result = model.transcribe(file_path)
    text = result["text"]
    return text

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/transcribe', methods=['GET'])
def transcribe():
    file_path = request.args.get('file_path')
    if file_path:
        return runSTT(file_path)
    else:
        return "Error: No file path provided."

if __name__ == '__main__':
    app.run(debug=True)