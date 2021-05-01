from datetime import datetime


def timeCheck():
    time = datetime.now()
    current_time = time.strftime('%H:%M:%S')
    return current_time
