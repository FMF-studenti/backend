import os
from datetime import datetime


def generate_upload_file_name():
    now = datetime.now()
    return [os.environ['NOTES_UPLOAD_PATH'], now.strftime('%Y%m%d%H%M%S') + '.pdf']

def list_uploaded_notes():
    path = os.environ['NOTES_UPLOAD_PATH']
    files = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f)) and f.endswith('.pdf')]
    return files

def handle_uploaded_note(f):
    name = generate_upload_file_name()
    with open('/'.join(name), 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)

    return {
        'pk': int(name[1][:-4]),
        'id': int(name[1][:-4]),
        'name': name[1]
    }

def move_registered_file_name(f, name):
    uploaded_path = os.environ['NOTES_UPLOAD_PATH']
    path = os.environ['NOTES_REGISTERED_PATH']
    new_name = name.title().replace(' ', '')[:20]

    # check if file exists
    orig_new_name = new_name
    c = 1
    while os.path.isfile(os.path.join(path, new_name + '.pdf')):
        new_name = orig_new_name + str(c)
        c += 1
    new_name += '.pdf'

    os.rename(os.path.join(uploaded_path, f), os.path.join(path, new_name))
    return new_name
