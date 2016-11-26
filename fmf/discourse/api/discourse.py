import os
from datetime import datetime
from . import api


def latest_topics(request):
    def find_poster(users, username):
        for user in users:
            if user['username'] == username:
                return user

    params = dict(request.GET)
    if 'type' in params.keys() and 'svet' in params['type']:
        category = 'studentski-organi/studentski-svet'
    else:
        category = None

    topics = []
    response = api.latest_topics(category)
    if 'users' in response:
        users = response['users']
        topic_list = response['topic_list']['topics']

        for topic in topic_list:
            poster = find_poster(users, topic['last_poster_username'])
            if not 'http' in poster['avatar_template']:
                poster['avatar_template'] = os.environ[
                    'DISCOURSE_HOST'] + poster['avatar_template']

            topics.append({
                'id': topic['id'],
                'title': topic['title'],
                'slug': topic['slug'],
                'updated': datetime.strptime(topic['bumped_at'][:-5], '%Y-%m-%dT%H:%M:%S'),
                'last_poster': poster['username'],
                'last_poster_avatar': poster['avatar_template'].replace('{size}', '64')
            })

        topics.sort(key=lambda topic: topic['updated'], reverse=True)

    if len(topics) > 6:
        return topics[:6]
    else:
        return topics


def user_info(request):
    user = request.user.social_auth.get(provider='discourse').extra_data
    info = api.user_info(user['username'])

    if not 'user' in info:
        return {
            'pk': 'me',
            'id': 0,
            'username': '',
            'name': '',
            'messages': 0,
            'avatar': '',
            'administrator': False,
            'error': True
        }

    messages = 0
    if 'private_messages_stats' in info['user']:
        messages = info['user']['private_messages_stats']['unread']

    data = {
        'pk': 'me',
        'id': info['user']['id'],
        'username': info['user']['username'],
        'name': info['user']['name'],
        'messages': messages,
        'avatar': os.environ['DISCOURSE_HOST'] + info['user']['avatar_template'].replace('{size}', '56'),
        'administrator': request.user and request.user.is_staff,
        'error': False
    }

    return data


def user_logout(request):
    user = request.user.social_auth.get(provider='discourse').extra_data
    return api.user_logout(user['external_id'])


def send_private_message(request):
    params = dict(request.POST)
    return api.send_private_message(params['title'][0], params['content'][0])
