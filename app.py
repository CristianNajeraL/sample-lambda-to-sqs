"""
AWS lambda handler to populate SQS
"""
import random


def lambda_handler(event, context):
    """
    Sample handler
    :return:
    """
    return {
        "random": f"This is master = {random.random()}"
    }
