import os
import requests


def common_url(call, authenticated=False, username=None):
    if authenticated and username is None:
        username = os.environ['DISCOURSE_ADMIN']

    if authenticated:
        return os.environ['DISCOURSE_HOST'] + '/' + call + '.json?api_key=' + os.environ['DISCOURSE_MASTER_API'] + '&api_username=' + username
    else:
        return os.environ['DISCOURSE_HOST'] + '/' + call + '.json'


def latest_topics(category=None):
    if not category is None:
        url = common_url('c/' + category + '/l/latest')
    else:
        url = common_url('latest')

    try:
        r = requests.get(url)
        return r.json()
    except requests.exceptions.ConnectionError:
        return {}


def user_info(username):
    url = common_url('users/' + username, True, username)

    try:
        r = requests.get(url)
        return r.json()
    except requests.exceptions.ConnectionError:
        return {}


def user_logout(user_id):
    url = common_url('admin/users/' + user_id + '/log_out', True)

    try:
        r = requests.post(url)
        return r.json()
    except requests.exceptions.ConnectionError:
        return {}


def send_private_message(title, content):
    # raw:wefwfwfwfwfwfwe
    # title:fefwefw
    # category:
    # is_warning:false
    # archetype:private_message
    # target_usernames:system
    # typing_duration_msecs:1600
    # composer_open_duration_msecs:31744
    # nested_post:true

    username = os.environ['DISCOURSE_ADMIN']
    api_key = os.environ['DISCOURSE_MASTER_API']

    data = {
        'api_key': api_key,
        'api_username': username,
        'title': title,
        'raw': content,
        'archetype': 'private_message',
        'target_usernames': 'test'  # username
    }

    url = common_url('posts')

    print(url)
    print(data)

    try:
        r = requests.post(url, data)
        return r.json()
    except requests.exceptions.ConnectionError:
        return {}
