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
	r = requests.get(url)

	return r.json()

def user_info(username):
	url = common_url('users/' + username, True, username)
	r = requests.get(url)

	return r.json()

def user_logout(user_id):
	url = common_url('admin/users/' + user_id + '/log_out', True)
	r = requests.post(url)

	return r.json()
