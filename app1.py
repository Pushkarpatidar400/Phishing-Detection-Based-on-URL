from flask import Flask, request, render_template
from bs4 import BeautifulSoup
import requests
import urllib.parse
from urllib.parse import urljoin

import json
import html


app = Flask(__name__)


@app.route('/',  methods=['GET','POST'])
def home():
    
    try:
        url = request.form['url']
        
    except:
        output = 'NA'

    return render_template('index.html', output=output)




if __name__ == '__main__':
    app.run(debug=True)