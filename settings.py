import xmltodict

settings = dict()

def load_settings():
    global settings
    with open('Data/settings.xml') as f:
        settings = xmltodict.parse(f.read())['settings']
    return settings

def check_min_setup():
    param_missing = False
    if not get_app_token():
        param_missing = True
        print('app_token not defined')
    if not get_client_id():
        param_missing = True
        print('client_id not defined')
    if not get_client_secret():
        param_missing = True
        print('client_secret not defined')
    if not get_bot_account():
        param_missing = True
        print('bot_account not defined')
    if not get_channel():
        param_missing = True
        print('channel not defined')

    if param_missing:
        #input('\nPress ENTER to exit')
        quit()

def get_app_token():
    return settings['bot_setup']['app_token']

def get_client_id():
    return settings['bot_setup']['client_id']

def get_client_secret():
    return settings['bot_setup']['client_secret']

def get_bot_account():
    return settings['bot_setup']['bot_account']

def get_prefix():
    return settings['bot_setup']['command_prefix']

def get_channel():
    return settings['bot_setup']['channel']

def get_logging():
    return settings['bot_setup']['logging']

def get_random_tf_id():
    return settings['bot_setup']['custom_rewards']['random_tf']

def get_direct_tf_id():
    return settings['bot_setup']['custom_rewards']['direct_tf']

def get_periodic_messages():
    return settings['bot_setup']['scheduled_messages']['messages']

def configure_periodic_messages():
    msg_list = settings['bot_setup']['scheduled_messages']['message']
    settings['bot_setup']['scheduled_messages'].pop('message')
    settings['bot_setup']['scheduled_messages'].update({'messages' : {}})
    if msg_list:
        msg_no = 0
        if isinstance(msg_list, str):
            settings['bot_setup']['scheduled_messages']['messages'].update({'1' : msg_list})
        else:
            for msg in msg_list:
                if msg:
                    msg_no = len(settings['bot_setup']['scheduled_messages']['messages']) + 1
                    settings['bot_setup']['scheduled_messages']['messages'].update({str(msg_no) : msg})
    return

def add_periodic_message(msg):
    msg_dict = get_periodic_messages()
    msg_no = len(msg_dict) + 1
    settings['bot_setup']['scheduled_messages']['messages'].update({str(msg_no) : msg})
    return

def remove_periodic_message(msg_no):
    msg_dict = get_periodic_messages()
    if msg_no in msg_dict.keys():
        settings['bot_setup']['scheduled_messages']['messages'].pop(msg_no)
        return True
    else:
        return False

def get_periodic_timer():
    if not settings['bot_setup']['scheduled_messages']['message_interval_minutes']:
        settings['bot_setup']['scheduled_messages'].update({'message_interval_minutes' : 15})
    return settings['bot_setup']['scheduled_messages']['message_interval_minutes']


def set_periodic_timer(time):
    settings['bot_setup']['scheduled_messages']['message_interval_minutes'] = time

def basics_enabled():
    enable = False
    value = settings['modules']['basics']['enable']
    if value.lower() == 'true':
        enable = True
    return enable

def get_twitter():
    return settings['modules']['basics']['twitter']

def get_discord():
    return settings['modules']['basics']['discord']

def emotes_enabled():
    enable = False
    value = settings['modules']['emotes']['enable']
    if value.lower() == 'true':
        enable = True
    return enable

def get_oof():
    return settings['modules']['emotes']['haurbuOof']

def get_heart():
    return settings['modules']['emotes']['haurbuHeart']

def raffle_enabled():
    enable = False
    value = settings['modules']['raffle']['enable']
    if value.lower() == 'true':
        enable = True
    return enable

def get_raffle_reminder_interval():
    return settings['modules']['raffle']['reminder_interval_minutes']

def quotes_enabled():
    enable = False
    value = settings['modules']['quotes']['enable']
    if value.lower() == 'true':
        enable = True
    return enable

def vip_quotes_allowed():
    allowed = False
    value = settings['modules']['quotes']['allow_vip']
    if value.lower() == 'true':
        allowed = True
    return allowed

def tf_enabled():
    enable = False
    value = settings['modules']['tf']['enable']
    if value.lower() == 'true':
        enable = True
    return enable

def rimworld_enabled():
    enable = False
    value = settings['modules']['rimworld']['enable']
    if value.lower() == 'true':
        enable = True
    return enable

def get_toolkit_path():
    return settings['modules']['rimworld']['toolkit_path']

def get_rimworld_mods():
    return settings['modules']['rimworld']['mods']

def avorion_enabled():
    enable = False
    value = settings['modules']['avorion']['enable']
    if value.lower() == 'true':
        enable = True
    return enable

def get_avorion_link():
    return settings['modules']['avorion']['profile_link']

def counter_enabled():
    enable = False
    value = settings['modules']['counter']['enable']
    if value.lower() == 'true':
        enable = True
    return enable

def vip_counter_allowed():
    allowed = False
    value = settings['modules']['counter']['allow_vip']
    if value.lower() == 'true':
        allowed = True
    return allowed