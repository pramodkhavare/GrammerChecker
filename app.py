from flask import Flask, render_template ,request
from model import CheckSpell 
spellchecker = CheckSpell() 


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/spell' ,methods =['GET' ,'POST'])
def spell():
    if request.method == 'POST':
        text = request.form['text'] 
        print(text)
        corrected_spell_text = spellchecker.correct_spelling(sentance=text)
        print(corrected_spell_text)
        corrected_grammer_text = spellchecker.correct_grammer(sentence=corrected_spell_text)
        print(corrected_grammer_text)
    return render_template(
            'index.html' ,corrected_text = corrected_spell_text ,corrected_grammar = corrected_grammer_text
        )



@app.route('/grammar',methods=['POST','GET'])
def grammar():
    if request.method == 'POST':
        file = request.files['file']
        readable_file = file.read().decode('utf-8',errors='ignore')
        corrected_file_text = spellchecker.correct_spelling(readable_file)
        corrected_file_grammar = spellchecker.correct_grammer(corrected_file_text)
        return render_template('index.html',corrected_file_text=corrected_file_text,corrected_file_grammar=corrected_file_grammar)




if __name__=="__main__":
    app.run(host='0.0.0.0' ,port=5000)