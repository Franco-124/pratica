"""import time
import notify2
from threading import Thread

def send_reminder(reminder_text, interval_minutes):
    def notify():
        print("Recordatorio de eventos iniciado")
        notify2.init("Daily reminder")
        while True:
            n = notify2.Notification("Daily reminder", reminder_text)
            n.set_timeout(30000)  # 30 seconds
            n.show()
            time.sleep(interval_minutes * 60)  # Convert minutes to seconds

    thread = Thread(target=notify)
    thread.daemon = True
    thread.start()"""