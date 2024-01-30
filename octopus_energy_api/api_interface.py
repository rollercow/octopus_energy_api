import requests
import pandas as pd
import time


class api:
    def __init__(self, api_key):
        self._api_key = api_key

    def create_session(self):
        session = requests.session()
        session.auth = (self._api_key, "")
        return session

    def run(self, url):
        session = self.create_session()
        response = session.request(method="GET", url=url)
        parsed = response.json()
        return parsed

    def pageFetcher(self, url):
        """Recursive function to fetch all pages of results"""
        response = self.run(url)
        if "results" in response:
            results = pd.DataFrame(response["results"])
        else:
            raise Exception(response)
        if response["next"]:
            # be kind to the API
            time.sleep(5)
            nextResults = self.pageFetcher(response["next"])
            return pd.concat([results, nextResults], ignore_index=True)
        else:
            return results
