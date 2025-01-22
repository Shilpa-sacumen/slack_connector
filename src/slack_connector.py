"""slack api """

import json
import logging
import logging.handlers

import requests


class Slack:
    """slack class
    """
    def __init__(self,token:str):
        """initialize method for slack class

        Args:
            token (str): slack api token
        """

        self.logger=logging.getLogger("my_logger")

        self.logger.setLevel(logging.DEBUG)

        self.handler=logging.FileHandler("slack.log",mode='w')

        self.formatter=logging.Formatter('%(process)d %(asctime)s %(name)s  %(levelname)s  %(message)s')

        self.handler.setFormatter(self.formatter)

        self.logger.addHandler(self.handler)

        self.headers={
                    'Authorization':f'Bearer {token}',
                    "Content-type": "application/x-www-form-urlencoded",
                    "Accept":"application/json"

                 }
        self.params={
                    'user':'USLACKBOT',
                 }    
    def user_info(self,base_url:str):
        """function for user.info api

        Args:
            base_url (str): base url of slack api
        """
        try:
            response=requests.get(base_url,headers=self.headers,params=self.params)
            response.raise_for_status() 
            self.logger.info(response.status_code)
            data=response.json()
            res=json.dumps(data,indent=4)
            self.logger.info(res)
            return response

             
        except requests.exceptions.HTTPError as e:
            self.logger.exception(f"HTTPError occured : {e}")
            raise
            
        except Exception as e:
            self.logger.exception(f'error occured {e}')
            raise

    def user_group_list(self,base_url:str):
        """function for usergroup.list api

        Args:
            base_url (str): base url of slack api
        """
        try:
            response=requests.get(base_url,headers=self.headers,)
            response.raise_for_status() 
            self.logger.info(response.status_code)
            data=response.json()
            res=json.dumps(data,indent=4)
            self.logger.info(res)
            return response
            
        except requests.exceptions.HTTPError as e:
            self.logger.exception(f"HTTPError occured : {e}")
            raise

        except Exception as e:
            self.logger.exception(f'error occered {e}')
            raise
 


