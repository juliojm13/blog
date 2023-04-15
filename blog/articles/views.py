from flask import Blueprint, render_template

articles = Blueprint(
    name='articles',
    import_name=__name__,
    static_folder='../static',
    url_prefix='/'
)
ARTICLES = [
    {
        'id': 1,
        'name': 'Django',
        'created_at': 'June 28, 2020',
        'comments_count': 10,
        'description': 'Django is amazing!!',
        'photo': '/static/images/image_5.jpg',
    },
    {
        'id': 2,
        'name': 'Flask',
        'created_at': 'Mar 15, 2021',
        'comments_count': 6,
        'description': 'Flask is okay!',
        'photo': '/static/images/image_6.jpg',
    },
    {
        'id': 3,
        'name': 'FastAPI',
        'created_at': 'Aug 29, 2020',
        'comments_count': 10,
        'description': 'FastAPI is killing it!!!!!',
        'photo': '/static/images/image_7.jpg',
    },
    {
        'id': 4,
        'name': 'All about python',
        'created_at': 'Oct 17, 2020',
        'comments_count': 3,
        'description': 'For all of us, we love python <3',
        'photo': '/static/images/image_8.jpg',
    },
]


@articles.route('/')
def index():
    return render_template('articles/welcome.html')


@articles.route('/articles')
def articles_list():
    return render_template('articles/articles_list.html', articles=ARTICLES)


@articles.route('/articles/<int:pk>')
def articles_detail(pk: int):
    article = ARTICLES[pk - 1]
    return render_template('articles/article_detail.html', article=article)
