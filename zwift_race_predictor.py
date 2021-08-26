from numpy import sign
import pandas as pd
import webscraper
from bs4 import BeautifulSoup

class ZwiftRacePredictor:

    def __init__(self):
        self.ws = webscraper.WebScraper()
        self.ws.login()

    def get_race_signups(self, race_id):
        html_raw = self.ws.get_page("https://zwiftpower.com/events.php?zid=" + str(race_id))
        html_processed = BeautifulSoup(html_raw, "lxml")

        signups = html_processed.find('table', {'id':'table_event_signups'})

        #file1 = open("signups.txt","w")
        #file1.write(str(html_raw))

        table_rows = signups.find_all('tr')

        res = []
        for tr in table_rows:
            td = tr.find_all('td')
            row = [tr.text.strip() for tr in td if tr.text.strip()]
            if row:
                res.append(row)

        return pd.DataFrame(res, columns=["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11"])

    def analyze_race(self, race_id):
        signups = self.get_race_signups(race_id)

zrp = ZwiftRacePredictor()

signups = zrp.get_race_signups("2255013")
print(signups)