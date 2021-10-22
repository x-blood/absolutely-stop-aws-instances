import json
from src.common import env
from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)


def send(slack_message):
    req = Request(
        env.get_slack_web_hook_url(),
        json.dumps(slack_message).encode('utf-8'))
    try:
        response = urlopen(req)
        response.read()
        logger.info("Message posted to %s", env.get_slack_web_hook_url())
    except HTTPError as e:
        logger.error("Request failed: %d %s", e.code, e.reason)
    except URLError as e:
        logger.error("Server connection failed: %s", e.reason)
