from flask import Flask, render_template, request, escape, session
from vsearch import search4letters
from DBcm import UseDatabase
from checker import check_logged_in
app = Flask(__name__)


# @app.route('/')
# def hello() -> '302':
#    return redirect('/entry')
#def log_request(req: 'flask_request', res: str) -> None:
#    with open('vsearch.log', 'a') as logfile:
#        print(req.form, req.remote_addr, req.user_agent, res, file=logfile, sep='|')

app.config['dbconfig'] = {'host': '127.0.0.1',
                          'user': 'soldvds',
                          'password': 'Vtyzpjdenktyz',
                          'database': 'vsearchlogDB', }


@app.route('/login')
def do_login() -> str:
    session['logged_in'] = True
    return 'You are now logged in.'


@app.route('/logout')
def do_logout() -> str:
    session.pop('logged_in')
    return 'You are now logged out.'


def log_request(req: 'flask_request', res: str) -> None:
    """Log details of the web request and the results"""
    with UseDatabase(app.config['dbconfig']) as cursor:
        _SQL = """insert into log
                  (phrase, letters, ip, browser_string, results)
                  values
                  (%s, %s, %s, %s, %s)"""
        cursor.execute(_SQL, (req.form['phrase'],
                              req.form['letters'],
                              req.remote_addr,
                              req.user_agent.browser,
                              res, ))


@app.route('/search4', methods=['POST'])
def do_search() -> 'html':
    phrase = request.form['phrase']
    letters = request.form['letters']
    title = 'Here are your results: '
    results = str(search4letters(phrase, letters))
    log_request(request, results)
    return render_template('results.html',
                           the_title=title,
                           the_letters=letters,
                           the_phrase=phrase,
                           the_results=results, )


@app.route('/')
@app.route('/entry')
def entry_page() -> 'html':
    return render_template('entry.html',
                           the_title='Welcome to search4letters on the web!')


#@app.route('/viewlog')
#def view_the_log() -> 'html':
#
#    contents = []
#    with open('vsearch.log') as log:
#        for line in log:
#            contents.append([])
#            for item in line.split('|'):
#                contents[-1].append(escape(item))
#
#    titles = ('Form Data', 'Remote_addr', 'User_agent', 'Results')
#    return render_template('viewlog.html',
#                           the_title='View Log',
#                           the_row_titles=titles,
#                           the_data=contents, )


@app.route('/viewlog')
@check_logged_in
def view_the_log() -> 'html':
    with UseDatabase(app.config['dbconfig']) as cursor:
        _SQL = """select phrase, letters, ip, browser_string, results 
                  from log"""
        cursor.execute(_SQL)
        contents = cursor.fetchall()
    titles = ('Phrase', 'Letters', 'Remote_addr', 'User_agent', 'Results')
    return render_template('viewlog.html',
                           the_title='View Log',
                           the_row_titles=titles,
                           the_data=contents, )


app.secret_key = 'YouWIllNeverGuessMySecretKey'


if __name__ == '__main__':
    app.run(debug=True)


