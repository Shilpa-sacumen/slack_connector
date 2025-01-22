# Slack connector
### Description
Created a sample slack connector 

## Functinality
To fetch the userinfo in slack workspace using the user.info endpoint<br>
To fetch the usergroup in slack workspace using the usergroup.list endpoint<br>

## Installation
```bash
git clone https://github.com/Shilpa-sacumen/slack_connector.git
```
```bash
cd slack_connector
```

```bash
pip install -r requirements.txt
```

## Configurations
### config.py
The `config.py` file contains all configurations required by the application<br>
api_token=your token <br>
base_url=your base url<br>
user_info=end point for userinfo<br>
user_group_list=end point for usergroup<br>

### logging
LOG_LEVEL='DEBUG"  #Logging level (DEBUG,INFO,WARNING,ERROR)<br>
LOG_HANDLER=FileHandler<br>
LOG_FORMATTER=%(process)d %(asctime)s %(name)s  %(levelname)s  %(message)s<br>
LOG_FILE=slack.log<br>

## To start connector
Steps to run connector<br>
1. create a virtual env and activate it.
2. Install all required packages using `requirements.txt`.
3. add required functions and unittest case for them.
4. Execute ```pytest path_of_testcase```.
5. To run functions defined execute `run.py` file. 