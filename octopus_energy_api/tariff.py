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
