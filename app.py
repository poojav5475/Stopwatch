from app import Flask, render_template

app = Flask(__name__)

@app.route('/')
def stopwatch():
    return render_template('C:\Codding\ML Ops\stopwatch\tamplet\stopwatch.html')

if __name__ == '__main__':
    app.run(debug=True)
