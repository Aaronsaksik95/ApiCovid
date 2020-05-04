from flask import Flask, render_template, url_for, request
import requests
import json

app = Flask(__name__)



@app.route("/")
def hello():    
   return render_template('ApiCovid.html')

@app.route("/",  methods=['POST'])
def test():
   pays = request.form['pays']  
   date = request.form['date'] + "T00:00:00Z"  
   COVID_API_URL = "https://api.covid19api.com/live/country/{}/status/confirmed/date/{}".format(
      pays, date)
   response = requests.get(COVID_API_URL)
   content = json.loads(response.content.decode('utf-8'))
   return render_template('ApiCovid.html', content=content, pays=pays)



if __name__ == "__main__":
    app.run(debug=True)