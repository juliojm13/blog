from flask import Blueprint, render_template

user = Blueprint(
    name='users',
    import_name=__name__,
    static_folder='../static',
    url_prefix='/users'
)

USERS = [
    {
        'id': 1,
        'name': 'Lola',
        'created_at': 'June 28, 2020',
        'comments_count': 10,
        'photo': '/static/images/image_1.jpg',
    },
    {
        'id': 2,
        'name': 'Juan',
        'created_at': 'Mar 15, 2021',
        'comments_count': 6,
        'photo': '/static/images/image_2.jpg',
    },
    {
        'id': 3,
        'name': 'Pedro',
        'created_at': 'Aug 29, 2020',
        'comments_count': 10,
        'photo': '/static/images/image_3.jpg',
    },
    {
        'id': 4,
        'name': 'Tom',
        'created_at': 'Oct 17, 2020',
        'comments_count': 3,
        'photo': '/static/images/image_4.jpg',
    },
]


@user.route('/')
def users_list():
    return render_template('users/users_list.html', users=USERS)


@user.route('/<int:pk>')
def users_detail(pk):
    user = USERS[pk - 1]
    return render_template('users/user_detail.html', user=user)
