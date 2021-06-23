from flask import Flask, render_template, request, redirect, escape
from Vsearch import search4letters
from DBcm import UseDatabase

app = Flask(__name__)
app.config['dbconfig'] = { 'host': '127.0.0.1',
	                       'user': 'vsearch',
	                       'password': 'vsearchpasswd',
	                       'database': 'vsearchlogDB',}

#@app.route('/')
#def hello() -> '302':
#    return redirect('/entry')
def log_request(req: 'flask_request', res: str) -> None:
    """Loguje szegóły żądania oraz wyniki."""

    with UseDatabase(app.config['dbconfig']) as cursor:
        _SQL = """insert into log
                (phrase, letters, ip, browser_string, result)
                values
                (%s,%s,%s,%s,%s)"""
        cursor.execute(_SQL, (req.form['phrase'],
                            req.form['letters'],
                            req.remote_addr,
                            req.user_agent.browser,
                            res, ))

    #with open('vsearch.log', 'a') as log:
    #    print(req.form, req.remote_addr, req.user_agent, res, file=log, sep='|')

@app.route('/search4', methods=['POST'])
def do_search() -> 'html':
    phrase = request.form['phrase']
    letters = request.form['letters']
    title = 'Oto Twoje wyniki:'
    results = str(search4letters(phrase, letters))
    log_request(request, results) 
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

@app.route('/viewlog')
def view_the_log() -> 'html':

    with UseDatabase(app.config['dbconfig']) as cursor:
        _SQL = """select phrase, letters, ip, browser_string, result
                from log"""
        cursor.execute(_SQL)
        contents = cursor.fetchall()
        
    titles = ('Fraza', 'Litery', 'Adres klienta', ' Agent uzytkownika', 'Wynik')

    return render_template('viewlog.html',
                            the_title = 'Widok logu',
                            the_row_titles = titles,
                            the_data = contents,) 
