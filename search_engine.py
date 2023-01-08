import requests

API_TOKEN = "WRrcjcrwiHhAQlw6FzIf"
URL = "https://the-one-api.dev/v2"


class SearchEngine:
    def __init__(self):
        self.headers = {
            "Authorization": "Bearer " + API_TOKEN,
        }

    def get_books(self):
        book_endpoint = URL + "/book"
        response = requests.get(url=book_endpoint, headers=self.headers).json()
        return response

    def get_book(self, book_id):
        book_endpoint = URL + "/book/" + book_id
        response = requests.get(url=book_endpoint, headers=self.headers).json()
        return response

    def get_movies(self):
        movie_endpoint = URL + "/movie"
        response = requests.get(url=movie_endpoint, headers=self.headers).json()
        return response

    def get_characters(self):
        character_endpoint = URL + "/character"
        response = requests.get(url=character_endpoint, headers=self.headers).json()
        return response

    def get_quotes(self):
        quote_endpoint = URL + "/quote"
        response = requests.get(url=quote_endpoint, headers=self.headers).json()
        return response

    def get_chapters(self):
        chapter_endpoint = URL + "/chapter"
        response = requests.get(url=chapter_endpoint, headers=self.headers).json()
        return response

    def chapters_in_book(self, book_id):
        endpoint = URL + "/book/" + book_id + "/chapter"
        response = requests.get(url=endpoint, headers=self.headers).json()
        return response

    def get_character(self, character_id):
        endpoint = URL + "/character/" + character_id
        response = requests.get(url=endpoint, headers=self.headers).json()
        return response

    def get_character_quote(self, character_id):
        endpoint = URL + "/character/" + character_id + "/quote"
        response = requests.get(url=endpoint, headers=self.headers).json()
        return response

    def get_movie(self, movie_id):
        endpoint = URL + "/movie/" + movie_id
        response = requests.get(url=endpoint, headers=self.headers).json()
        return response
