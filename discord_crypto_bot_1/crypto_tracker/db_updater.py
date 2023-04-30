"""
Модуль для переодического обновления базы данных.

Запросы отправляемые к api, обновляются переодически, потому нет смысла делать новый запрос для каждой команды пользователя.
Будет рациональнее сохранять результат каждые N времени (смотрите db_updater, file body, _update_db_job, @_schedule.every(30).seconds.do)?,
И передавать результат пользователю.
"""


# requirements imports begin {

import schedule as _schedule
import os as _os


from dotenv import load_dotenv as _load_dotenv
from requests import request as _request
from functools import wraps as _wraps
from time import sleep as _sleep
from decimal import Decimal as _Decimal

# } requirements imports end



# relative imports begin {

if __name__ == '__main__':
    _load_dotenv()

    from db import database
    
else:
    from .db import database

# } relative imports end



# file body begin {

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



def start_updating(delay: int | float = 1):
    while True:
        try:
            _schedule.run_pending()
            _sleep(delay)


        except KeyboardInterrupt:
            break

# } file body end



# other begin {

if __name__ == '__main__':
    start_updating()


__all__ = [n for n in globals() if n[:1] != '_']

# } other end
