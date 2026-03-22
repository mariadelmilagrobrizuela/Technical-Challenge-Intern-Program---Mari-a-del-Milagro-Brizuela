class Series:
    """
    Although the class could be omitted, since the core of the model is the Episode class, I 
    added the Series class in a lightweight way to help organize the results and make the model 
    clearer, without introducing unnecessary complexity.
    """

    def __init__(self, series_name):
        self.series_name = series_name
        self.episodes = []
    
    
    def add_episode(self, episode):
        self.episodes.append(episode)