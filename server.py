from flask import Flask, render_template

app = Flask(__name__)

@app.route('/table')
def Show_Table():
    individuals_list = [
        {'first_name' : 'Michael', 'last_name' : 'Choi'},
        {'first_name' : 'John', 'last_name' : 'Supsupin'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
]

    for individual in individuals_list:
        individual['full_name'] = individual['first_name'] + ' ' + individual['last_name'] 

    return render_template('index.html', individuals_list=individuals_list)

if __name__=="__main__":  
    app.run(debug=True, port=5001)