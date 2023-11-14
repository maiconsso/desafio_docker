from flask import Flask, render_template, request, redirect, url_for 
from flask_mysqldb import MySQL


app = Flask(__name__) 
app.config['SECRET_KEY'] = 'contatos'
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'fatec'
app.config['MYSQL_DB'] = 'bancocontatos'

mysql = MySQL(app)

@app.route('/', methods=['GET'])
def index():
    return render_template("index.html")

@app.route('/contato', methods=['GET', 'POST'])
def contatos():
    if request.method == "POST":
        details = request.form
        email = details['email']
        assunto = details['assunto']
        texto = details['texto']

        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO contatos (con_email, con_assunto, con_texto) VALUES (%s, %s, %s)", (email, assunto, texto))
        mysql.connection.commit()
        cur.close()
    return redirect(url_for('index'))


@app.route('/mensagem')
def mensagem():
    cur = mysql.connection.cursor()

    lista = 'select * from contatos'
    cur.execute(lista)
    lista = cur.fetchall()
    cur.close()
    return render_template('mensagem.html', lista=lista)

if __name__ == "__main__":
    app.run(debug=True)
