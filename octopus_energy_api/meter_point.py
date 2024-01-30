import octopus_energy_api.meter


class meter_point:
    def __init__(self, api, meter_point_data):
        self._api = api
        self.meter_point_data = meter_point_data
        for k, v in meter_point_data.items():
            setattr(self, k, v)
        self.m = []
        for thismeter in self.meters:
            am = octopus_energy_api.meter.meter(api, self.mpan, thismeter)
            self.m.append(am)
