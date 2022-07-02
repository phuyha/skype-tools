from skpy import Skype
import config


def send_message(content, mention):
    try:
        sk = Skype(config.SENDER_USER_ID, config.PASSWORD)
        # skc = SkypeChats(sk)
        # recent_contact = skc.recent()
        ch = sk.chats[config.GROUP_ID]
        ch.sendMsg(''.join([mention, content]), rich=True)
    except Exception as e:
        raise e
