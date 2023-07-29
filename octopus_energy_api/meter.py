class meter:
    def __init__(self, api, mpan, meter_data):
        self._api = api
        self.mpan = mpan
        self.meter_data = meter_data
        for k, v in meter_data.items():
            setattr(self, k, v)
        foo = self._api.discover_meter(self)
        self.start = foo[0]
        self.end = foo[1]
        self.count = foo[2]

    def __str__(self):
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
