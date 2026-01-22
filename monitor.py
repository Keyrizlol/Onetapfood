import time
import threading

status = {
    "last_order": None,
    "state": "idle",
    "eta": None,
    "service": None
}

def simulate_delivery_progress():
    while True:
        if status["state"] == "on_the_way":
            if status["eta"] > 0:
                status["eta"] -= 1
            else:
                status["state"] = "delivered"
        time.sleep(60)
        

def start_monitoring():
    monitor_thread = threading.Thread(target=simulate_delivery_progress)
    monitor_thread.daemon = True
    monitor_thread.start()
