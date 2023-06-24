class EducationalContent:
    def __init__(self):
        self.articles = []
        self.videos = []

    def add_article(self):
        # Kod do dodawania artykułu
        article = input("Enter article title: ")
        self.articles.append(article)
        print("Article added:", article)

    def add_video(self):
        # Kod do dodawania wideo
        video = input("Enter video title: ")
        self.videos.append(video)
        print("Video added:", video)
