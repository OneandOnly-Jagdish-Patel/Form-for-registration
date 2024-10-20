from flask import Flask, render_template, url_for, request,redirect
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('form.html')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    email = request.form['email']
    Phone = request.form['phone']
    mandal = request.form['occupation']
    october31 = request.form['ans']
    november1 = request.form['1november']
    november2 = request.form['2november']

    mandal_dict = {
    'NorthYork' : 'https://sheetdb.io/api/v1/gxmmko96zjybv',
    'Etobicoke' : 'https://sheetdb.io/api/v1/sbr6q3rnah0vk',
    'Brampton' : 'https://sheetdb.io/api/v1/g6s9ezoz5cbio',
    'master_url' : 'https://sheetdb.io/api/v1/176gnwf3j8d1n',
    }
    user_data = {
            "name" : name,
            "email" : email,
            "Phone" : Phone,
            "mandal" : mandal,
            "october31" : october31,
            "november1" : november1,
            "november2" : november2
        }

    data = requests.get(mandal_dict['master_url']).json()
    for i in data:
        if i['Email'] == email:
            return redirect(url_for('error'))
    
    row = {
        "sheet1" : {
            "Name" : name,
            "Email" : email,
            "Phone" : Phone,
            "Mandal" : mandal,
            "31st OCTOBER" : october31,
            "1st NOVEMBER" : november1,
            "2nd NOVEMBER" : november2
        }
    }
    response = requests.post(mandal_dict[mandal], json=row)
    response2 = requests.post(mandal_dict['master_url'], json=row)
    print(response.status_code)
    print(response2.status_code)

    return render_template('thankyou.html',value=user_data)
@app.route('/error')
def error():
    return render_template('error.html')

@app.route('/thankyou')
def thankyou():
    return render_template('thankyou.html')


if __name__ == '__main__':
    app.run(debug=True)
