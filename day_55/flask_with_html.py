from flask import Flask

app = Flask(__name__)


@app.route('/home/<name>')
def get_html(name):
    return f'<h1 style="color:green; text-align:center; font-size:80px" >Hello {name}</h1>' \
           f'<p>CEN I HAV A PUSI PLEESE.</p>'


if __name__ == '__main__':
    app.run(debug=True)
