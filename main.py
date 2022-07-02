import schedule
import time
import config
from service import send_message
from libs import Log, date_time


log = Log('send_skype_message')
log.info('Run job send skype message!!!')

SUNDAY = 6
REUNIFICATION_DAY = '30-04-2022'
HUNG_KING_DAY = '09-04-2022'
COMPENSATORY_DAY = '02-05-2022'


def send_skype_message():
    try:
        today = date_time.datetime.today()
        # filter days unnecessary for sending message
        if today.weekday() == SUNDAY \
                or today.strftime('%d-%m-%Y') == HUNG_KING_DAY \
                or today.strftime('%d-%m-%Y') == REUNIFICATION_DAY \
                or today.strftime('%d-%m-%Y') == COMPENSATORY_DAY:
            return None

        mention = '<at id="{}">{}</at> '.format(config.RECEIVER_USER_ID, config.RECEIVER_USERNAME)
        content = 'Some message you want to send'
        send_message(content, mention)
        log.info(f'Sent message at {date_time.current_datetime_with_tz()}')
    except Exception as e:
        log.error(f'Error at send_skype_message: {str(e)}')


schedule.every().day.at(config.JOB_TIMELINE).do(send_skype_message)
while True:
    schedule.run_pending()
    time.sleep(1)
