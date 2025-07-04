from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('form.html')

@app.route('/submit', methods=['POST'])
def submit_form():
    name = request.form['name']
    email = request.form['email']
    message = request.form['message']

    with open('form.txt', 'a') as f:
        f.write(f'Имя: {name}\n')
        f.write(f'Email: {email}\n')
        f.write(f'Сообщение: {message}\n')
        f.write('---\n')

    return render_template('form_result.html', name=name, email=email, message=message)
