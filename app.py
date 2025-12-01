from flask import Flask, render_template, request
from scanner import scan_many_ports

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/scan", methods=["POST"])
def scan():
    target = request.form.get("target")
    ports_input = request.form.get("ports")

    if "-" in ports_input:
        start, end = map(int, ports_input.split("-"))
        ports = list(range(start, end + 1))
    else:
        ports = [int(p.strip()) for p in ports_input.split(",")]

    results = scan_many_ports(target, ports)

    return render_template("results.html", target=target, results=results)

if __name__ == "__main__":
    app.run(debug=True)
