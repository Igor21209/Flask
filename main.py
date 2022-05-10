from flask import Flask, redirect, render_template

app = Flask(__name__)
a = [{'name': 'Alex', 'id': 1, 'surname': 'Turner', 'age': 33}, {'name': 'Thome', 'id': 2, 'surname': 'York', 'age': 50},
     {'name': 'Igor', 'id': 3, 'surname': 'First', 'age': 21}]


@app.route('/')
def hello_world():
    return render_template('main.html')


@app.route('/users', methods=["POST", "GET"])
def users():
    return render_template('user.html', users=a)


@app.route('/info/<id>', methods=["POST", "GET"])
def info(id):
    s = int(id)
    for i in a:
        if i['id'] == s:
            inf = i
    return render_template('info.html', inf=inf)


if __name__ == '__main__':
    app.run()