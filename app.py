from flask import Flask, render_template, request, jsonify

app = Flask(__name__)    

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        return jsonify(request.form)
    return render_template("form.html")

if __name__ == '__main__':
    app.run(port=5000, debug=True)  # PUERTO Y MODO PRUEBAS
