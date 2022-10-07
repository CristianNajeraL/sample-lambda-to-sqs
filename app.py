"""
AWS lambda handler to populate SQS
"""
import random


def lambda_handler(event, context):
    """
    Sample handler
    :return:
    """
    print(event)
    return {
        "random": f"This is develop = {random.random()}"
    }
