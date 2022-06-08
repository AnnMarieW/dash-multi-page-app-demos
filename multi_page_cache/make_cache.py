from flask_caching import Cache
from dash import get_app

import datetime

import pandas as pd
import time


app = get_app()
serverside_cache = Cache(
    app.server,
    config={
        # 'CACHE_TYPE': 'redis',
        # Note that filesystem cache doesn't work on systems with ephemeral
        # filesystems like Heroku.
        "CACHE_TYPE": "filesystem",
        "CACHE_DIR": "cache-directory",
        # should be equal to maximum number of users on the app at a single time
        # higher numbers will store more data in the filesystem / redis cache
        "CACHE_THRESHOLD": 200,
    },
)


def get_dataframe(session_id):

    @serverside_cache.memoize()
    def query_and_serialize_data(session_id):
        # expensive or user/session-unique data processing step goes here

        # simulate a user/session-unique data processing step by generating
        # data that is dependent on time
        now = datetime.datetime.now()

        # simulate an expensive data processing task by sleeping
        time.sleep(3)

        df = pd.DataFrame(
            {
                "time": [
                    str(now - datetime.timedelta(seconds=15)),
                    str(now - datetime.timedelta(seconds=10)),
                    str(now - datetime.timedelta(seconds=5)),
                    str(now),
                ],
                "values": ["a", "b", "a", "c"],
            }
        )
        return df.to_json()

    return pd.read_json(query_and_serialize_data(session_id))
