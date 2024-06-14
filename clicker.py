import time
import pyautogui

def autoclicker(interval_seconds=1):
    try:
        while True:
            x, y = pyautogui.position()  # Fare pozisyonunu al
            pyautogui.click(x, y)  # Tıklama işlemi
            time.sleep(interval_seconds)  # Belirli bir süre bekleyin
    except KeyboardInterrupt:
        print("Otomatik tıklama işlemi durduruldu.")

# Otomatik tıklama işlemini başlatın (saniyede bir tıklama)
autoclicker(interval_seconds=1)
