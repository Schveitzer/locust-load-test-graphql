import json
import os

from locust import TaskSet, task, FastHttpUser, constant


class Bitquery(TaskSet):

    def on_start(self):
        self.x_api_key = os.getenv('API_KEY')

    @task
    def get_bitcoin_daily_transaction_vol(self):

        body_graphql = json.loads(
            r'''{
                "variables":{
                    "from": "2020-10-10",
                    "till": "2020-10-10"
                },
                "query": "query($from: ISO8601DateTime, $till: ISO8601DateTime){bitcoin { transactions(options: {desc: \"date.date\"}, date: {since: $from, till: $till}, ){txVolUSD: inputValue(calculate: sum in: USD) date{date} } } }"
            }'''
        )

        headers = {"Content-type": "application/json", "Accept": "application/graphql", "X-API-KEY": self.x_api_key}

        with self.client.post('/', name="Bitcoin_Vol", catch_response=True, headers=headers, json=body_graphql) as response:

            if response.status_code == 200:
                json_response = json.loads(response.text)
                if 'transactions' in json_response['data']['bitcoin']:
                    response.success()
                else:
                    response.failure(f" Object transactions not in response:{json_response}")
            else:
                response.failure(f" Error status code received:{response.status_code}")


class TestUser(FastHttpUser):
    tasks = [Bitquery]
    wait_time = constant(1)
    host = "https://graphql.bitquery.io"
