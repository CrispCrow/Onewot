from typing import NamedTuple

from wotbwrapper import WotbClient, User

wotbclient = WotbClient(application_id='anything')

def get_user_info(username: str) -> User:
    user = wotbclient.get_user('test')
    return user
