from pickle import TRUE
from flask import Blueprint, render_template
from .models import Book
api = Blueprint('Blueprint', __name__, url_prefix='/api')


@api.route('/')
def index():
    books = Book.query.all()
    return render_template('sample.html')

#if __name__ == "__main__":
 #   app.run(debug=TRUE,port=5006)
