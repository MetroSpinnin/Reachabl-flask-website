#import the necessary modules
from flask import Flask 
from flask import url_for
from flask import render_template

#initialize the application
app = Flask(__name__)

#create valid routing for the pages
@app.route('/')
@app.route('/index')
@app.route('/home')
def homepage(): 
	return render_template('home.html')

@app.route('/about')
@app.route('/about-us')
def aboutReachabl():
	return render_template('about.html')

@app.route('/moments')
@app.route('/Reachablmoments')
def momentsReachabl():
	return render_template('moments.html')

@app.route('/monetization')
@app.route('/Reachablmonetization')
def monetizeReachabl():
	return render_template('monetization.html')

@app.route('/data')
@app.route('/Reachabldata')
def dataReachabl():
	return render_template('data.html')

@app.route('/press')
@app.route('/Reachablpress')
def pressReachabl():
	return render_template('press.html')

@app.route('/contact')
@app.route('/Reachablcontact')
def contactReachabl():
	return render_template('contact.html')

@app.route('/terms')
@app.route('/Reachablterms')
def termsReachabl():
	return render_template('terms.html')

@app.route('/policy')
@app.route('/Reachablpolicy')
def policyReachabl():
	return render_template('privacy-policy.html')

@app.route('/docs-sdk')
@app.route('/Reachabldocs-sdk')
def docsReachabl():
	return render_template('docs-sdk.html')

@app.route('/api-license')
@app.route('/Reachablapi-license')
def licenseReachabl():
	return render_template('api-license.html')

#run main application Loop

if __name__ == '__main__':
	app.run(debug = True)