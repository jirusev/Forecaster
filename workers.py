from PyQt5.QtCore import *
import json
import os
import requests
from urllib.parse import urlencode


class Signals(QObject):
    '''
    Signals definition
    '''
    finished = pyqtSignal()
    error = pyqtSignal(str)
    result = pyqtSignal(dict, dict)


class ForecasterWorker(QRunnable):
    '''
    Thread for updates.
    Do the API calls in a thread to prevent freezing.
    '''
    signals = Signals()

    def __init__(self, location):
        super(ForecasterWorker, self).__init__()
        self._location = location

    @pyqtSlot()
    def run(self):
        """
        run(self)
        Make API calls
        """
        try:
            # Create data container, matching the api url fields names
            api_data = dict(
                q=self._location,
                appid=os.environ.get("FORECASTER_API_KEY")
            )

            # Format the weather_url
            weather_url = 'http://api.openweathermap.org/data/2.5/weather?%s&units=metric' % urlencode(api_data)
            response = requests.get(weather_url)
            weather_data = json.loads(response.text)

            # Check response
            if not response.ok:
                raise Exception(weather_data['message'])

            forecast_daily = 'http://api.openweathermap.org/data/2.5/forecast?%s&units=metric&cnt=5' % urlencode(
                api_data)
            response = requests.get(forecast_daily)
            forecast_daily_data = json.loads(response.text)

            # Just in case
            if not response.ok:
                raise Exception(forecast_daily['message'])

            # Emit the received data
            self.signals.result.emit(weather_data, forecast_daily_data)

        except Exception as e:
            self.signals.error.emit(str(e))

        # Emit that the thread has finished
        self.signals.finished.emit()
