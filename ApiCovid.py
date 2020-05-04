from flask import Flask, render_template, url_for, request
import requests
import json

app = Flask(__name__)


@app.route("/")
def hello():
   COVID_API_URL_PAYS = "https://api.covid19api.com/summary"
   responsePays = requests.get(COVID_API_URL_PAYS)
   contentPays = json.loads(responsePays.content.decode('utf-8'))
   countries = contentPays["Countries"]
   return render_template('ApiCovid.html', countries=countries)



@app.route("/",  methods=['POST'])
def apiCovid():
   COVID_API_URL_PAYS = "https://api.covid19api.com/summary"
   responsePays = requests.get(COVID_API_URL_PAYS)
   contentPays = json.loads(responsePays.content.decode('utf-8'))
   countries = contentPays["Countries"]
   pays = request.form['pays']
   date = request.form['date'] + "T00:00:00Z"
   COVID_API_URL = "https://api.covid19api.com/live/country/{}/status/confirmed/date/{}".format(
        pays, date)
   response = requests.get(COVID_API_URL)
   content = json.loads(response.content.decode('utf-8'))
   dataMin = []
   dataMax = []
   for i in content:
      paysTest = i['Country']
      dataMin.append(paysTest.lower())
      dataMax.append(paysTest)
   if pays in dataMin or pays in dataMax :
        return render_template('ApiCovid.html', content=content, pays=pays, countries=countries)
   else:
        return render_template("500.html"), 500


if __name__ == "__main__":
    app.run(debug=True)
