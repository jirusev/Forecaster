from PyQt5.QtCore import QThreadPool
from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox
import json
from UI.MainWindow import Ui_MainWindow
from helpers import from_ts_to_time_of_day, path_countries, set_icon
from workers import ForecasterWorker


class MainWindow(QMainWindow, Ui_MainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self._countries = {}
        self.setupUi(self)

        self._load_countries()
        self._load_cities()

        self.cmbCountry.currentIndexChanged.connect(self._load_cities)
        self.btnLoadWeather.pressed.connect(self._load)

        self.tPool = QThreadPool()

        self.show()

    def _load_countries(self) -> None:
        with open(path_countries, encoding='utf-8') as file:
            self._countries = json.load(file)

        for country in self._countries['data']:
            self.cmbCountry.addItem(country['country'])

    def _load_cities(self) -> None:
        country = self.cmbCountry.currentText()

        if not country:
            return

        for c in self._countries['data']:
            if c['country'] == country:
                self.cmbCity.clear()
                for data in c['cities']:
                    self.cmbCity.addItem(data)
                break

    def _warn(self, message) -> None:
        QMessageBox.warning(self, self.tr("Warning"),
                            self.tr(message))

    def _load(self) -> None:
        if not self.cmbCity.currentText():
            QMessageBox.warning(self, "Warning", "Please select a city.")
            return

        worker = ForecasterWorker(self.cmbCity.currentText())
        worker.signals.result.connect(self._weather_result)
        worker.signals.error.connect(self._warn)

        self.tPool.start(worker)

    def _weather_result(self, weather_data: dict, forecast_daily_data: dict) -> None:
        """

        :param weather_data:
        :param forecast_data:
        """
        self.lblLatitude.setText("%.2f °" % weather_data['coord']['lat'])
        self.lblLongitude.setText("%.2f °" % weather_data['coord']['lon'])

        self.lblWind.setText("%.2f m/s" % weather_data['wind']['speed'])

        self.lblTemp.setText("%.1f °C" % weather_data['main']['temp'])
        self.lblPressure.setText("%d" % weather_data['main']['pressure'])
        self.lblHumidity.setText("%d" % weather_data['main']['humidity'])

        self.lblSunrise.setText(from_ts_to_time_of_day(weather_data['sys']['sunrise']))

        self.lblWeather.setText("%s (%s)" % (
            weather_data['weather'][0]['main'],
            weather_data['weather'][0]['description']
        ))

        set_icon(self.lblIcon, weather_data['weather'])

        for i, daily in enumerate(forecast_daily_data['list'], 1):
            getattr(self, 'lblDay%d' % i).setText(from_ts_to_time_of_day(daily['dt']))
            set_icon(getattr(self, 'lblIcon%d' % i), daily['weather'])
            getattr(self, 'lblTemp%d' % i).setText("%.1f °C" % daily['main']['temp'])


if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    app.exec_()
