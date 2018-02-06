# Google Style Guide --> https://google.github.io/styleguide/pyguide.html

import webbrowser

class Movie():

    """This Class Provides A Way To Store Movie Related Information"""

    valid_ratings = ["G","PG","PG-13","R"]

    def __init__(self,movie_title,movie_storyline, poster_image, trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
