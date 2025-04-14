from datetime import datetime, timezone
import pandas as pd


class tarrif:
    def __init__(self, api, tariff_code, fromDT, toDT):
        self._api = api
        self.fuel = tariff_code[0]
        self.registers = tariff_code[2]
        self.productCode = tariff_code[5:-2]
        self.GSPGroup = tariff_code[-1]
        self.fromDT = datetime.fromisoformat(fromDT)
        if toDT:
            self.toDT = datetime.fromisoformat(toDT)
        else:
            self.toDT = datetime.now(timezone.utc)

    def __str__(self):
        return (
            "Fuel - "
            + self.fuel
            + ", Registers - "
            + self.registers
            + ", Product Code - "
            + self.productCode
            + ", GSP Group - "
            + self.GSPGroup
        )

    def tariffCode(self):
        return self.fuel + "-" + self.registers + "R-" + self.productCode + "-" + self.GSPGroup

    def lookup(self, start: datetime = None, end: datetime = None):
        if not start:
            start = self.fromDT
        if not end:
            end = self.toDT
        if self.fuel == "E" and int(self.registers) == 1:
            start = start.astimezone(timezone.utc).isoformat().replace("+00:00", "Z")
            end = end.astimezone(timezone.utc).isoformat().replace("+00:00", "Z")
            url = self._api._urls().tariff_url(self.productCode, self.tariffCode(), start, end)
            dfPrice = self._api._api.pageFetcher(url)
            dfPrice["valid_from"] = pd.to_datetime(dfPrice["valid_from"], utc=True)
            dfPrice["valid_to"] = pd.to_datetime(dfPrice["valid_to"], utc=True)
            # trim the end date to when we joined the tarrif
            setend = {}
            setend["valid_to"] = self.toDT
            df2 = pd.DataFrame([setend])
            dfPrice.update(df2)
            # turn it upside down
            dfPrice = dfPrice.sort_values("valid_from").reset_index(drop=True)
            # trim the start date to when we joined the tarrif
            setstart = {}
            setstart["valid_from"] = self.fromDT
            df2 = pd.DataFrame([setstart])
            dfPrice.update(df2)

            return dfPrice
        else:
            print("Only single register electric meters implemented")
