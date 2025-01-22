""" to run the slack connector """

from src.slack_connector_call import start

try:
    start()
except Exception as e:
    raise e