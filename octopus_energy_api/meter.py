class meter:
    def __init__(self, api, mpan, meter_data):
        self._api = api
        self.mpan = mpan
        self.meter_data = meter_data
        for k, v in meter_data.items():
            setattr(self, k, v)
        print(self._api.discover_meter(self))
