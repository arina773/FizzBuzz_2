from flask import Flask, render_template, request


app = Flask(__name__)
result = ''


@app.route('/', defaults={'n': 0})
@app.route('/<n>')
def start(n):
    if n == 0:
        return render_template('index.html', n=int(n))

    elif n.isdigit():
        return render_template('index.html', n=int(n))
    else:
        return render_template('index.html', n=0)


@app.route('/submit')
def submit():
        return render_template('submit.html')


@app.route("/result/<n>", methods=['POST', 'GET'])
def result(n):
    if request.method == 'GET':
        return render_template('submit.html')
    elif request.method == 'POST':
        n = list(request.form.values())[0]
        if n.isdigit():
            return render_template('index.html', n=int(n))
        else:
            return render_template('index.html', n=0)


if __name__ == '__main__':
    app.run(debug=True)






# @app.route('/form')
# def form():
#     return render_template('form.html')
#
#
# @app.route('/data', methods = ['POST', 'GET'])
# def data():
#     if request.method == 'GET':
#         return f"The URL /data is accessed directly. Try going to '/form' to submit form"
#     if request.method == 'POST':
#         form_data = request.form
#         return render_template('data.html',form_data=form_data)

