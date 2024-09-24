from .repository import get_all_users, create_user, get_user, update_user, remove_user


def fetch_all_users():
    users = get_all_users()
    return users


def add_user(id, name, email, password, role):
    create_user(id, name, email, password, role)
    return


def fetch_user(id):
    user = get_user(id)
    return user


def modify_user(user_id, name=None, email=None, password=None, role=None):
    update_user(user_id, name, email, password, role)
    return


def delete_user(user_id):
    remove_user(user_id)
    return
