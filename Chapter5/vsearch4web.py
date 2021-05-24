from flask import Flask, render_template, request, redirect
from Vsearch import search4letters

app = Flask(__name__)
#Utworzenie instancj Flask i przypisanie jej do zmiennej app

#@app.route('/')
#def hello() -> '302':
#    return redirect('/entry')

@app.route('/search4', methods=['POST'])
def do_search() -> 'html':
    phrase = request.form['phrase']
    letters = request.form['letters']
    title = 'Oto Twoje wyniki:'
    results = str(search4letters(phrase, letters)) 
    return render_template('results.html',
                            the_phrase = phrase,
                            the_letters = letters,
                            the_title = title,
                            the_result = results,)
@app.route('/')
@app.route('/entry')
def entry_page():
    return render_template('entry.html',
                            the_title = 'Witaj na stronie internetowej search4letters!')