from flask import Flask, render_template, redirect,request
import extractor
import pandas as pd
from joblib import load

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
    return render_template('index.html')

@app.route('/check',methods=['GET','POST'])
def check():
    if request.method == 'POST':
        url = request.form['url']  # Use request.form.get('url') to safely retrieve the form data
        data = extractor.extract_features_from_url(url)
        data = pd.DataFrame(data, index=[0])
        model = load('svm.joblib')
        ans = model.predict(data)
        if ans[0]:
            return redirect(url)
        else:
            return render_template('failure.html')
    else:
        # Handle GET request (if needed)
        pass
if __name__ == '__main__':
    app.run(debug=True)

