import webbrowser
class Movie():
    """Class provides a way to store movies and other information about them"""
    validRatings = ["G","PG", "PG 12", "R"]

    def __init__(self, title, storyline, poster_image, trailer):
        self.title = title
        self.storyline = storyline
        self.poster_img_url = poster_image
        self.trailer_youtube = trailer
    
    def trailer(self):
        webbrowser.open(self.trailer_youtube)
        
