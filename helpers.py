from datetime import datetime
import os

from PyQt5.QtGui import QPixmap

path_countries: str = r"resources/countries.json"
path_images: str = r"resources/images"


def from_ts_to_time_of_day(param: int) -> str:
    date = datetime.fromtimestamp(param)
    return date.strftime("%I%p").lstrip("0")


def set_icon(q_label, weather: list) -> None:
    path = os.path.join(path_images, "%s.png" %
                        weather[0]['icon'])
    q_label.setPixmap(QPixmap(path))
