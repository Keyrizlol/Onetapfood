import random
import time

def fake_delivery_service(order):
    """
    Simuliert die Antwort eines Lieferdienstes.
    Tut so, als würde ein externer Server antworten.
    """
    print(" → Anfrage beim Lieferdienst wird verarbeitet...")

    time.sleep(1)  # simulierte Serverzeit

    # Simuliere Zufallsereignisse
    if random.random() < 0.01:  # 1% Chance auf Fehler
        return {
            "status": "error",
            "message": "Lieferdienst nicht erreichbar"
        }

    return {
        "status": "ok",
        "delivery_time": f"{random.randint(20, 50)} min",
        "accepted_by": random.choice(["Pizza Pazzo", "Burger Hof", "Asia Star"]),
        "order_details": order
    }


def send_order_to_service(order):
    """
    Nimmt die fertige Bestellung von der Orderlogik entgegen
    und schickt sie an den simulierten Lieferdienst.
    """
    print("→ Sende Bestellung an Lieferdienst...")

    response = fake_delivery_service(order)

    if response["status"] == "ok":
        print("✔ Bestellung erfolgreich übermittelt!")
        print("   Lieferdienst:", response["accepted_by"])
        print("   Lieferzeit:", response["delivery_time"])
        return response

    else:
        print("Fehler:", response["message"])
        return response



def test_api_layer():
    """
    Testet den API-Layer unabhängig von der echten Orderlogik.
    """
    print("\n=== TEST DER KOMMUNIKATIONS-SCHICHT ===")

    test_order = {
        "produkt": "Pizza Salami",
        "menge": 1,
        "preis": 12.50,
        "adresse": "Musterstraße 5",
        "zahlungsart": "Barzahlung"
    }

    print("Testbestellung:", test_order)
    print("---------------------------------------")

    result = send_order_to_service(test_order)

    print("---------------------------------------")
    print("Ergebnis des Tests:", result)
    print("=== TEST BEENDET ===\n")


if __name__ == "__main__":
    test_api_layer()



