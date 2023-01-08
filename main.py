from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from datetime import datetime
from search_engine import SearchEngine

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)

search_engine = SearchEngine()

books = search_engine.get_books()
movies = search_engine.get_movies()
characters = search_engine.get_characters()
quotes = search_engine.get_quotes()
chapters = search_engine.get_chapters()
# data = [books, movies, chapters, quotes, chapters]

categories = [
    {"name": "Books", "description": 'List of all "The Lord of the Rings" books', "data": books},
    {"name": "Movies",
     "description": 'List of all movies, including the "The Lord of the Rings" and the "The Hobbit" trilogies',
     "data": movies},
    {"name": "Characters",
     "description": "List of characters including metadata like name, gender, realm, race and more",
     "data": characters},
    # {"name": "Quotes", "description": "List of all movie quotes", "data": quotes},
    # {"name": "Chapters", "description": "List of all book chapters", "data": chapters},
]


@app.route('/')
def home():
    return render_template("index.html", categories=categories)


@app.route("/<string:category>")
def show_category(category):
    items_to_render = None
    for item in categories:
        # print(item["name"], category)
        if category == item["name"]:
            items_to_render = item["data"]
            # print(items_to_render["docs"])
            return render_template(f"{category.lower()}.html", items=items_to_render)
    return render_template("index.html", categories=categories)


@app.route("/book/<string:book_id>/chapter")
def show_chapters(book_id):
    chapters_in_book = search_engine.chapters_in_book(book_id)
    book = search_engine.get_book(book_id)
    return render_template("chapters.html", chapters=chapters_in_book, book=book)


@app.route("/character/<string:character_id>")
def show_character(character_id):
    character = search_engine.get_character(character_id)
    character_quotes = search_engine.get_character_quote(character_id)
    return render_template("character.html", character=character, quotes=character_quotes)


@app.route("/movie/<string:movie_id>")
def get_movie(movie_id):
    movie = search_engine.get_movie(movie_id)
    return render_template("movies.html", items=movie)


@app.context_processor
def inject_now():
    return {'now': datetime.utcnow()}


if __name__ == "__main__":
    app.run(debug=True)
