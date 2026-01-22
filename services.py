import random
import time
import json

def fake_delivery_service(order):
    """Simuliert einen Lieferdienst."""
    time.sleep(1)

    if random.random() < 0.12:
        return {"status": "error", "message": "Lieferdienst offline"}

    return {
        "status": "ok",
        "service": random.choice(["McDonalds", "BurgerKing", "Dominos"]),
        "eta": random.randint(20, 50),
        "order": order
    }


def send_order(order):
    """API-Layer → sendet Bestellung an Lieferdienst."""
    response = fake_delivery_service(order)
    return response


def test_api():
    """Manuelle Testfunktion."""
    test_order = {
        "produkt": "Pizza Salami",
        "menge": 1,
        "adresse": "Musterstraße 10",
        "zahlung": "Barzahlung"
    }

    result = send_order(test_order)
    print("API-Test:", json.dumps(result, indent=4))
    return result
