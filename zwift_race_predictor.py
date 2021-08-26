from numpy import sign
import pandas as pd
import webscraper
from bs4 import BeautifulSoup

class ZwiftRacePredictor:

    def __init__(self):
        self.ws = webscraper.WebScraper()
        self.ws.login()
        self.rider = pd.DataFrame

    def get_race_data(self, race_id):

        # get signup data from zwiftpower
        raw_data = self.ws.get_page("https://zwiftpower.com/events.php?zid=" + str(race_id))

        # format raw data
        return BeautifulSoup(raw_data, "lxml")

    def get_rider_data(self, rider_id):

        # get rider data from zwiftpower
        raw_data = self.ws.get_page("https://zwiftpower.com/profile.php?z=" + str(rider_id))

        # format raw data
        return BeautifulSoup(raw_data, "lxml")

    def process_race_signups(self, race_id):

        # get race data
        formated_data = self.get_race_data(race_id)

        # extract signup table from race data
        signups = formated_data.find('table', {'id':'table_event_signups'})

        # split signup table into rows, creating the field (array of riders)
        field = signups.find_all('tr')

        rider_list = []

        # each row in field is one rider
        for row in field:

            # split row into riders attributes
            attributes = row.find_all('td')

            # remove overhead
            row = [row.text.strip() for row in attributes]

            # add rider to list
            if row:
                rider_list.append(row)

        # coverting list into dataframe for easier handling
        self.rider = pd.DataFrame(rider_list, columns=["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12"])

    def process_race_results(self, race_id):

        # get race data
        formated_data = self.get_race_data(race_id)

        # TODO write code to extract race results
        print("nothing implemented yet :(")

    def process_rider_data(self, rider_id):

        # get rider data
        self.get_rider_data(rider_id)

        # TODO write code to extract rider attributes
        print("nothing implemented yet :(")

    def analyze_pre_race(self, race_id):

        # get race signup data
        self.process_race_signups(race_id)

        # TODO write code to analyze race results
        print("nothing implemented yet :(")

    def analyze_post_race(self, race_id):
        
        # get race result data
        self.process_race_results(race_id)

        # TODO write code to analyze race results
        print("nothing implemented yet :(")

zrp = ZwiftRacePredictor()
zrp.analyze_pre_race("2256709")