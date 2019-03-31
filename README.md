## Reachabl-flask-website

Basically this is a demo file of the Reachabl website built in Python (Flask framework), it is a very simple application that would enable anyone play around with flask and also gives an insight into testing the application, it does not rather treat the application as a package, but modules can be imported, also in the test files the `unittest.main()` enables the running of the appliication showing errors and failures

## Testing the application

Actually for the testing, i used unittest for testing and had to test all the available routes in the application with the functions below
`import os`
`import unittest`
`from app import app`

`#create the class for testing the app`

`class RoutingTests(unittest.TestCase)`

`"""
declare the setUp functions and Teardown funcs
and start basic testing of the Routes
"""`

## Deploying the app

After downloading the Zip folder, extract it and set up a virtual environment, then run the application using `python app.py` and to test the application use the command `python app_test.py`

