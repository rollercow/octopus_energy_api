class meter_point:
    def __init__(self, urls, api, meter_point_data):

        self._urls = urls
        self._api = api
        
        self.meter_point_data = meter_point_data
        for k, v in meter_point_data.items():
            setattr(self, k, v)
    