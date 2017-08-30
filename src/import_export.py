from json import dump, load
from os import path


def get_path(file_name):
    relative = path.dirname(__file__)
    return path.join(relative, 'keys', file_name)


def import_public_key(a_file_name):
    public_key = 0

    a_file_name = get_path(a_file_name)
    if path.exists(a_file_name):
        with open(a_file_name, 'r') as f:
            public_key = load(f)

    return public_key


def import_private_key(a_file_name):
    private_key = 0

    a_file_name = get_path(a_file_name)
    if path.exists(a_file_name):
        with open(a_file_name, 'r') as f:
            private_key = load(f)

    return private_key


def export_public_key(public_key, a_file_name):
    a_file_name = get_path(a_file_name)
    with open(a_file_name, 'w+') as f:
        dump(public_key, f)


def export_private_key(private_key, k, a_file_name):
    private_key = [private_key, k]
    a_file_name = get_path(a_file_name)
    with open(a_file_name, 'w+') as f:
        dump(private_key, f)

