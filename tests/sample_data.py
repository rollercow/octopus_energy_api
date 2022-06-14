sample_account_details = {
    "number": "A-123AB123",
    "properties": [
        {
            "id": 1234567,
            "moved_in_at": "2020-01-01T00:00:00Z",
            "moved_out_at": None,
            "address_line_1": "1, SAMPLE DRIVE",
            "address_line_2": "LONDON",
            "address_line_3": "",
            "town": "",
            "county": "",
            "postcode": "AB1 2AB",
            "electricity_meter_points": [
                {
                    "mpan": "1234567890123",
                    "profile_class": 2,
                    "consumption_day": None,
                    "consumption_night": None,
                    "meters": [
                        {
                            "serial_number": "A12A12345",
                            "registers": [
                                {
                                    "identifier": "L",
                                    "rate": "NIGHT",
                                    "is_settlement_register": True,
                                },
                                {"identifier": "N", "rate": "DAY", "is_settlement_register": True},
                            ],
                        },
                        {
                            "serial_number": "12A1234567",
                            "registers": [
                                {"identifier": "1", "rate": "", "is_settlement_register": True},
                                {"identifier": "2", "rate": "", "is_settlement_register": True},
                            ],
                        },
                    ],
                    "agreements": [
                        {
                            "tariff_code": "E-2R-FIX-12M-20-09-21-C",
                            "valid_from": "2020-01-01T00:00:00Z",
                            "valid_to": "2021-12-06T00:00:00Z",
                        }
                    ],
                    "is_export": False,
                }
            ],
            "gas_meter_points": [],
        }
    ],
}

sample_consumption = {
    "count": 15,
    "next": None,
    "previous": None,
    "results": [
        {
            "consumption": 0.405,
            "interval_start": "2021-06-17T17:00:00+01:00",
            "interval_end": "2021-06-17T17:30:00+01:00",
        },
        {
            "consumption": 0.843,
            "interval_start": "2021-06-17T17:30:00+01:00",
            "interval_end": "2021-06-17T18:00:00+01:00",
        },
        {
            "consumption": 0.503,
            "interval_start": "2021-06-17T18:00:00+01:00",
            "interval_end": "2021-06-17T18:30:00+01:00",
        },
        {
            "consumption": 0.077,
            "interval_start": "2021-06-17T18:30:00+01:00",
            "interval_end": "2021-06-17T19:00:00+01:00",
        },
        {
            "consumption": 0.138,
            "interval_start": "2021-06-17T19:00:00+01:00",
            "interval_end": "2021-06-17T19:30:00+01:00",
        },
        {
            "consumption": 0.073,
            "interval_start": "2021-06-17T19:30:00+01:00",
            "interval_end": "2021-06-17T20:00:00+01:00",
        },
        {
            "consumption": 0.082,
            "interval_start": "2021-06-17T20:00:00+01:00",
            "interval_end": "2021-06-17T20:30:00+01:00",
        },
        {
            "consumption": 0.087,
            "interval_start": "2021-06-17T20:30:00+01:00",
            "interval_end": "2021-06-17T21:00:00+01:00",
        },
        {
            "consumption": 0.068,
            "interval_start": "2021-06-17T21:00:00+01:00",
            "interval_end": "2021-06-17T21:30:00+01:00",
        },
        {
            "consumption": 0.037,
            "interval_start": "2021-06-17T21:30:00+01:00",
            "interval_end": "2021-06-17T22:00:00+01:00",
        },
        {
            "consumption": 0.155,
            "interval_start": "2021-06-17T22:00:00+01:00",
            "interval_end": "2021-06-17T22:30:00+01:00",
        },
        {
            "consumption": 0.102,
            "interval_start": "2021-06-17T22:30:00+01:00",
            "interval_end": "2021-06-17T23:00:00+01:00",
        },
        {
            "consumption": 0.069,
            "interval_start": "2021-06-17T23:00:00+01:00",
            "interval_end": "2021-06-17T23:30:00+01:00",
        },
        {
            "consumption": 0.045,
            "interval_start": "2021-06-17T23:30:00+01:00",
            "interval_end": "2021-06-18T00:00:00+01:00",
        },
        {
            "consumption": 0.026,
            "interval_start": "2021-06-18T00:00:00+01:00",
            "interval_end": "2021-06-18T00:30:00+01:00",
        },
    ],
}

sample_meter_data = {"gsp": "_C", "mpan": "1234567890123", "profile_class": 2}

sample_account_number = "A-123AB123"
sample_api_key = "ab_live_a4b7A1AB98abcdeABCd1Ef2g"
