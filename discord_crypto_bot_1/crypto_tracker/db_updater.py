if __name__ == '__main__':
    from dotenv import load_dotenv as _load_dotenv
    _load_dotenv()


import schedule as _schedule
import os as _os


from functools import wraps as _wraps
from time import sleep as _sleep
from decimal import Decimal as _Decimal
from requests import request as _request
from json import loads as _loads


from db import database





def _catch_exceptions(job_func):
    @_wraps(job_func)
    def wrapper(*args, **kwargs):
        try:
            return job_func(*args, **kwargs)

        except Exception as error:
            print(repr(error))
            # return _schedule.CancelJob

    return wrapper


def _get_crypto_ranks():
    headers = {
        'x-access-token': _os.getenv('CRYPTO_RANKS_API_TOKEN'),
    }
    
    response = _request("GET", r"https://api.coinranking.com/v2/coins?uuids[]=razxDUgYGNAdQ&uuids[]=Qwsogvtv82FCd", headers=headers)

    return response.text
    # return response.json()


@_schedule.every(30).seconds.do
@_catch_exceptions
def _update_db_job():
    ranks = _get_crypto_ranks()
    database.update(ranks)
    print("!!")



def start_updating(delay=1):
    while True:
        _schedule.run_pending()
        _sleep(delay)



if __name__ == '__main__':
    start_updating()