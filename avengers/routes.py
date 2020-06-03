from avengers import app
from flask import render_template, request
#Import for Forms
from avengers.forms import Form

#Home Route
@app.route('/',methods = ['GET','POST'])
def home():
    return render_template("home.html")

#Registered Phone Number
@app.route('/phonebook', methods = ['GET','POST'])
def phonebook():
    names = {"Iron Man":773-996-6005 , "Thor":708-788-7010, "Wasp":847-340-6792,"Ant-Man":217-715-1349,  "Hulk":217-620-7346 }
    return render_template("phonebook.html", names = names)
#UPDATE
@app.route('/update', methods=['GET', 'POST'])
def update():
    update = Form()
    if request.method == "POST" and update.validate():   
        names = update.names.data
        numbers = update.numbers.data
        print('\n', names, numbers)
    return render_template('update.html',update=update)