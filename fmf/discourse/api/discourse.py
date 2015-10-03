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

    response = api.latest_topics(category)
    users = response['users']
    topic_list = response['topic_list']['topics']

    topics = []
    for topic in topic_list:
        poster = find_poster(users, topic['last_poster_username'])
        if not 'http' in poster['avatar_template']:
            poster['avatar_template'] = os.environ['DISCOURSE_HOST'] + poster['avatar_template']

        topics.append({
            'id': topic['id'],
            'title': topic['title'],
            'slug': topic['slug'],
            'updated': datetime.strptime(topic['bumped_at'][:-5], '%Y-%m-%dT%H:%M:%S'),
            'last_poster': poster['username'],
            'last_poster_avatar': poster['avatar_template'].replace('{size}', '64')
        })

    topics.sort(key=lambda topic: topic['updated'], reverse=True)

    return topics[:6]

def user_info(request):
    user = request.user.social_auth.get(provider='discourse').extra_data
    info = api.user_info(user['username'])

    data = {
        'pk': 'me',
    	'id': info['user']['id'],
    	'username': info['user']['username'],
    	'name': info['user']['name'],
    	'messages': info['user']['private_messages_stats']['unread'],
    	'avatar': os.environ['DISCOURSE_HOST'] + info['user']['avatar_template'].replace('{size}', '56'),
        'administrator': request.user and request.user.is_staff
    }

    return data

def user_logout(request):
    user = request.user.social_auth.get(provider='discourse').extra_data
    return api.user_logout(user['external_id'])
