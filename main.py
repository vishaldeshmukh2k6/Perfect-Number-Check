from flask import Flask, render_template, request

app = Flask(__name__)

def is_perfect(num):
    total = 0
    for i in range(1, num):
        if num % i == 0:
            total += i
    return total == num

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    if request.method == 'POST':
        try:
            num = int(request.form['number'])
            if is_perfect(num):
                result = f"{num} is a Perfect Number"
            else:
                result = f"{num} is Not a Perfect Number"
        except ValueError:
            result = "Please enter a valid number."
    return render_template('index.html', result=result)

if __name__ == "__main__":
    app.run(debug=True, port=5006)
