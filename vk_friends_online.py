import vk
import getpass
from time import sleep

APP_ID = 6125813


def get_user_login():
    user_login = input('Login: ')
    return user_login


def get_user_password():
    user_password = getpass.getpass()
    return user_password


def get_online_friends(login, password):
    online_friends_names = []
    try:
        session = vk.AuthSession(
                app_id=APP_ID,
                user_login=login,
                user_password=password,
                scope='friends'
        )
        
    except vk.exceptions.VkAuthError as error:
        print('Login failed: %s' % error)
    else:
        vk_api = vk.API(session)
        online_friends_ids = vk_api.friends.getOnline()
        for id in online_friends_ids:
            friend_data = vk_api.users.get(user_id=id)
            online_friends_names.append('%s %s' % (friend_data[0]['first_name'], friend_data[0]['last_name']))
            # only three requests per second allowed by API
            sleep(0.33)
    finally:
        return online_friends_names




def output_friends_to_console(friends_online):
    for friend in friends_online:
        print(friend)


if __name__ == '__main__':
    login = get_user_login()
    password = get_user_password()
    friends_online = get_online_friends(login, password)
    output_friends_to_console(friends_online)
