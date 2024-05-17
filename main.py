from flask import Flask, render_template, request
from mod import get_modulo_one_num
app = Flask(__name__)

@app.route("/", methods=('GET', 'POST'))
def index():
    if request.method == 'POST':
        digits = int(request.form['digits'])
        modulo = int(request.form['modulo'])
        if digits >32 :
            return "Error: max digit supported 32"
        if modulo<1 or modulo>97:
            return "Error: Support modulo range 1-97"
        print(digits)
        print(modulo)
        num = get_modulo_one_num(digits, modulo)
        return "Your modulo 1 Number is: "+ str(num)+"\n\n\n\n\n\n   .....refresh this page to generate a new number"

    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)