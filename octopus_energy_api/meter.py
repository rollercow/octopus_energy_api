from datetime import datetime, timezone
import pandas as pd
import time


class meter:
    def __init__(self, api, mpan, meter_data):
        self._api = api
        self.mpan = mpan
        self.meter_data = meter_data
        for k, v in meter_data.items():
            setattr(self, k, v)
        data = self._api.discover_meter(self)
        if data:
            self.hasData = True
            self.start = data[0]
            self.end = data[1]
            self.count = data[2]
        else:
            self.hasData = False
        print(self.printMeter())

    def printMeter(self):
        if self.hasData:
            return (
                "MPAN: "
                + self.mpan
                + " / Serial: "
                + self.serial_number
                + " / DataPoints: "
                + str(self.count)
                + " / From: "
                + self.start
                + " / End: "
                + self.end
            )
        else:
            return "MPAN: " + self.mpan + " / Serial: " + self.serial_number

    def consumption(self, start: datetime, end: datetime):
        """Get all consumption data between 2 datetimes"""
        start = start.astimezone(timezone.utc).isoformat().replace("+00:00", "Z")
        end = end.astimezone(timezone.utc).isoformat().replace("+00:00", "Z")
        url = self._api._urls().consumption_url(self.mpan, self.serial_number, start, end)
        return self._consumptionFetcher(url)

    def _consumptionFetcher(self, url):
        """Recursive function to fetch all pages of consumption"""
        response = self._api._api.run(url)
        if "results" in response:
            results = pd.DataFrame(response["results"])
        else:
            raise Exception(response)
        if response["next"]:
            # be kind to the API
            time.sleep(5)
            nextResults = self._consumptionFetcher(response["next"])
            return pd.concat([results, nextResults], ignore_index=True)
        else:
            return results
