from flask import Flask, render_template, request, jsonify
from transformers import pipeline
import PyPDF2

app = Flask(__name__)

generator = pipeline("text-generation", model="gpt2")

def generate_mcq(text):
    prompt = f"Generate a multiple-choice question from the following text: '{text}' with four answer options."
    result = generator(prompt, max_new_tokens=100, num_return_sequences=1) #Here is the change
    return result[0]['generated_text']

def extract_text_from_pdf(pdf_file):
    text = ""
    try:
        pdf_reader = PyPDF2.PdfReader(pdf_file)
        for page_num in range(len(pdf_reader.pages)):
            page = pdf_reader.pages[page_num]
            text += page.extract_text()
    except Exception as e:
        print(f"Error extracting PDF: {e}")
        return None
    return text

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if 'pdf_file' in request.files:
            pdf_file = request.files['pdf_file']
            if pdf_file.filename != '':
                text = extract_text_from_pdf(pdf_file)
                if text:
                    question = generate_mcq(text)
                    return jsonify({'question': question})

        elif 'text_input' in request.form:
            text = request.form['text_input']
            question = generate_mcq(text)
            return jsonify({'question': question})

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)