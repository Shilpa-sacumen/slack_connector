""" call function for userinfo and usergroup endpoints"""

from configparser import ConfigParser

from src.slack_connector import Slack

config=ConfigParser()
config.read("config/config.cfg")

api_token=config['api_credentials']['api_token']
base_url=config['base_url']['base_url']
userinfo_endpoint=config['end_ponits']['user_info']
usergroup_endpoint=config['end_ponits']['user_group_list']
obj=Slack(token=api_token)

def start():
    """
    function to start slack connector
    """

    obj.user_info(base_url+userinfo_endpoint)
    obj.user_group_list(base_url+usergroup_endpoint)
