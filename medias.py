import webbrowser

class Movie():
    def __init__(self, movie_title, movie_storyline, movie_image, movie_trailer):
        self.title = movie_title
        self.storyline = movie_storyline
        self.image = movie_image
        self.trailer = movie_trailer

    def show_trailer(self):
        webbrowser.open(self.trailer)
