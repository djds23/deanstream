from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/_add_numbers')
def add_numbers():
    a = request.args.get('a',0,type=int)
    b = request.args.get('b',0,type=int)
    return jsonify(result=a+b)

@app.route('/test')
def test():
    return render_template('testenv.html')

if __name__ == '__main__':
    app.run(debug=True)
