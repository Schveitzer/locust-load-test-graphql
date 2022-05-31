#Load Testing a GraphQL API with Locust in Python

Example of load testing with locust in a grapql api in Python

>To run this project, you need an access key for the Bitquery api, it can be obtained by accessing:
> https://graphql.bitquery.io/ide/

## Requirements
- Python >= 3.6 - [How install Pytohn](https://www.python.org/downloads/)
- Pip >= 20.0.x - [How install pip](https://pip.pypa.io/en/stable/installing/)

## Getting Started
Install dependencies:

```bash
$ pip install --no-cache-dir -r requirements.txt
```

## Running

Export API Key:

```bash
$ export API_KEY=BQYB1jH8KufYHYRfNOOXE3IAATpdjQEE
```

Execute Locust
```bash
$ locust -f bitquery_graphql.py
```
