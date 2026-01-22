from flask import Flask, render_template, jsonify
import json, time
from services import send_order
from monitor import status, start_monitoring

app = Flask(__name__)


# ORDERLOGIK

def create_order():
    order = {
        "produkt": "Random Gericht",
        "timestamp": time.time(),
        "adresse": "Sir's Palace",
        "zahlung": "Barzahlung"
    }
    return order


@app.route("/order")
def hunger_order():
    
    order = create_order()
    response = send_order(order)

    if response["status"] == "ok":
        status["state"] = "on_the_way"
        status["eta"] = response["eta"]
        status["service"] = response["service"]
        status["last_order"] = order
        write_log(response)
        return jsonify({"message": "Bestellung erfolgreich!", "details": response})
    else:
        status["state"] = "error"
        write_log(response)
        return jsonify({"message": "Fehler!", "details": response})



# LOGGING

def write_log(entry):
    with open("logs/orders.log", "a") as f:
        f.write(json.dumps(entry) + "\n")



# DASHBOARD

@app.route("/")
def dashboard():
    return render_template("dashboard.html", status=status)


if __name__ == "__main__":
    start_monitoring()
    app.run(host="0.0.0.0", port=5000, debug=True)
