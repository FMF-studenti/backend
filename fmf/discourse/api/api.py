import os
import requests

def common_url(call, username=None):
	if username is None:
		username = os.environ['DISCOURSE_ADMIN']

	return os.environ['DISCOURSE_HOST'] + '/' + call + '.json?api_key=' + os.environ['DISCOURSE_MASTER_API'] + '&api_username=' + username

def user_info(username):
	url = common_url('users/' + username, username)
	r = requests.get(url)

	return r.json()

def user_logout(user_id):
	url = common_url('admin/users/' + user_id + '/log_out')
	r = requests.post(url)

	return r.json()
