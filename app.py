from flask import Flask, render_template, request
import numpy as np

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')

@app.route("/predict", methods = ['POST'])
def predict():
    if request.method == 'POST':
        wisata = request.form['wisata']
        rating = request.form['rating']
        arr = np.arr([[wisata, rating]])
        pred = model.predict(arr)
        return render_template('home.html', data=pred)
        
    
if __name__ == "__main__":
    app.run(debug=True)