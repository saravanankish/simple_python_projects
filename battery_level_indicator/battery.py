import psutil
import time
from plyer import notification

while True:
    battery = psutil.sensors_battery()
    percent = battery.percent

    notification.notify(
        title="Battery Percentage",
        message=str(percent) + "%  Battery Remaining",
        timeout=10
    )

    time.sleep(60 * 60)
    continue
