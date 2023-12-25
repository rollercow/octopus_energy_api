class meter:
    def __init__(self, api, mpan, meter_data):
        self._api = api
        self.mpan = mpan
        self.meter_data = meter_data
        for k, v in meter_data.items():
            setattr(self, k, v)
        data = self._api.discover_meter(self)
        if data:
            self.data = True
            self.start = data[0]
            self.end = data[1]
            self.count = data[2]
        else:
            self.data = False

    def __str__(self):
        if self.data:
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
