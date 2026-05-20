from datetime import datetime
import pytz


class TimeUtils:

    @staticmethod
    def get_current_time():
        india = pytz.timezone("Asia/Kolkata")

        return datetime.now(india).strftime("%Y-%m-%d %H:%M:%S")