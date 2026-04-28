# main file in the project
# let's import the flask
from flask import Flask, render_template  # type: ignore[reportMissingImports]
import os # importing operating system module

app = Flask(__name__)

@app.route('/') # this decorator create the home route
def home ():
    techs = ['HTML', 'CSS', 'Flask', 'Python']
    name = '60 Days Of Python Programming'
    return render_template('home.html', techs=techs, name = name, title = 'Home')

@app.route('/about')
def about():
    name = '60 Days Of Python Programming'
    return render_template('about.html', name = name, title = 'About Us')



if __name__ == '__main__':
    # for deployment we use the environ
    # to make it work for both production and development
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)

# to run the application write in the terminal: python app.py, after you run python app.py, you can see the output in the terminal and also you can open the browser and go to http://localhost:5000/ to see the output.