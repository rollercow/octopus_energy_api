from octopus_energy_api.api_interface import api
from octopus_energy_api.account import account
from octopus_energy_api.urls import urls
from octopus_energy_api.meter_point import meter_point
from datetime import datetime
import statistics


class oe_api:
    def __init__(self, account_number, api_key, mpan=None, serial_number=None):

        self._urls = urls

        self._api = api(api_key)

        # setup account
        account_url = self._urls.accounts_url(account_number)
        account_details = self._api.run(account_url)
        self.account = account(account_details)
        self.properties = []
        for property in self.account.properties:
            p = {}
            meters_points = []
            for k, v in property.items():
                if "meter_points" not in k:
                    print(k)
            for elec_meter_point in property["electricity_meter_points"]:
                mp = meter_point(self, elec_meter_point)
                meters_points.append(mp)
            p["meters"] = meters_points
            self.properties.append(p)

    def account_details(self):
        """See account data"""

        url = self._urls.accounts_url(self.account.number)

        response = self._api.run(url)

        return response

    def discover_meter(self, meter):
        url = self._urls.meter_discovery_url(meter.mpan, meter.serial_number)
        answer = self._api.run(url)["results"]
        if len(answer) == 0:
            return False
        start = answer[0]["interval_start"]
        url = self._urls.meter_discovery_url(meter.mpan, meter.serial_number, "-period")
        foo = self._api.run(url)
        end = foo["results"][0]["interval_end"]
        count = foo["count"]
        return [start, end, count]

    def products(self):
        """Get all product info for Octopus Energy"""

        response = self._api.run(self._urls.products_url())

        return response

    @classmethod
    def convert_datetime_to_tz(cls, time):

        format_tz = "%Y-%m-%dT%H:%M:%S%z"

        return time.strftime(format_tz)

    @classmethod
    def convert_to_datetime(cls, time):

        format_tz = "%Y-%m-%dT%H:%M:%S%z"

        return datetime.strptime(time, format_tz)

    def consumption(self, start: datetime, end: datetime):
        """Get all consumption data between 2 datetimes"""

        if (end - start).days > 365:
            raise RuntimeError("time difference is greater than one year")

        start = self.convert_datetime_to_tz(start)
        end = self.convert_datetime_to_tz(end)

        url = self._urls.consumption_url(self.account.mpan, self.account.serial_number, start, end)
        response = self._api.run(url)

        return response["results"]

    def consumption_total(self, start: datetime, end: datetime):
        """Calculates the amount of kWh used in the timeframe given, returns the value as a float"""

        consumption = self.consumption(start, end)

        total_consumption = 0

        for record in consumption:
            total_consumption += record["consumption"]

        total_consumption = float("%.2f" % total_consumption)

        return total_consumption

    def consumption_mean(self, start: datetime, end: datetime):
        """Calculates the average kWh used in 30 minutes within the timeframe given, returns the value as a float"""

        consumption = self.consumption(start, end)

        consumption_list = []

        for record in consumption:
            consumption_list.append(record["consumption"])

        average = float("%.2f" % float(sum(consumption_list) / len(consumption_list)))

        return average

    def consumption_median(self, start: datetime, end: datetime):
        """Median of all rates during times stated"""

        consumption = self.consumption(start, end)

        consumption_list = []

        for record in consumption:
            consumption_list.append(record["consumption"])

        median = statistics.median(consumption_list)

        return median

    def consumption_cost(self, start: datetime, end: datetime, rate: float):
        """Calculates the cost of electricity given during the times stated.
        Does not check actual unit rates per hour."""

        consumption = self.consumption(start, end)

        total_consumption = 0

        for record in consumption:
            total_consumption += record["consumption"]

        total_consumption = float("%.2f" % total_consumption)

        return total_consumption * rate

    def meter_point(self):

        url = self._urls.meter_point_url(self.account.mpan)

        response = self._api.run(url)

        return response
