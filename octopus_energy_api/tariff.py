from datetime import datetime, timezone


class tarrif:
    def __init__(self, api, tariff_code, fromDT, toDt):
        self._api = api
        self.fuel = tariff_code[0]
        self.registers = tariff_code[2]
        self.productCode = tariff_code[5:-2]
        self.GSPGroup = tariff_code[-1]

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

    def lookup(self, start: datetime, end: datetime):
        if self.fuel == "E" and int(self.registers) == 1:
            start = start.astimezone(timezone.utc).isoformat().replace("+00:00", "Z")
            end = end.astimezone(timezone.utc).isoformat().replace("+00:00", "Z")
            url = self._api._urls().tariff_url(self.productCode, self.tariffCode(), start, end)
            return self._api._api.pageFetcher(url)
        else:
            print("Only single register electric meters implemented")
