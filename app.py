from flask import Flask,render_template

app = Flask(__name__, template_folder='C://Users//MOHAM//Desktop//Astrowebsite//templates', static_folder='C://Users//MOHAM//Desktop//Astrowebsite//static')


@app.route("/")
def home():
    return render_template('index.html')

@app.route("/Community/")
def about():
    return render_template('Community.html')

if __name__=="__main__":
    app.run(debug=True)