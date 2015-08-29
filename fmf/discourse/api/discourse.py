import os
from . import api

def user_info(request):
    user = request.user.social_auth.get(provider='discourse').extra_data
    info = api.user_info(user['username'])

    data = {
        'pk': 'me',
    	'id': info['user']['id'],
    	'username': info['user']['username'],
    	'name': info['user']['name'],
    	'messages': info['user']['private_messages_stats']['unread'],
    	'avatar': os.environ['DISCOURSE_HOST'] + info['user']['avatar_template'].replace('{size}', '56')
    }

    return data