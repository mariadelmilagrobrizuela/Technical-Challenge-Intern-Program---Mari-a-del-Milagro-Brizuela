from utils.text_utils import normalize_text
from utils.date_utils import is_valid_date


class Episode:
    def __init__(self, series_name, season_number, episode_number, episode_title, air_date):
        self.series_name = series_name
        self.season_number = season_number
        self.episode_number = episode_number
        self.episode_title = episode_title
        self.air_date = air_date
    

    def normalize(self):
        """
        I decided to leave special characters in titles or series names—unchanged, because 
        they may be part of the original and meaningful information.
        """

        self.series_name = normalize_text(self.series_name)
        self.episode_title = normalize_text(self.episode_title)


    def _is_valid_number(self, value):
        try:
            return int(value) > 0
        
        except:
            return False


    def clean(self):
        if not self._is_valid_number(self.season_number):
            self.season_number = 0
        else:
            self.season_number = int(self.season_number)

        if not self._is_valid_number(self.episode_number):
            self.episode_number = 0
        else:
            self.episode_number = int(self.episode_number)

        if not self.episode_title:
            self.episode_title = "Untitled Episode"
        
        if not is_valid_date(self.air_date):
            self.air_date = "Unknown"


    def is_discardable(self):
        if not self.series_name:
            return True
        
        if self.episode_number == 0 and self.episode_title == "Untitled Episode" and self.air_date == "Unknown":
            return True
        
        return False