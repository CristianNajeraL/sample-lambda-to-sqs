FROM amazon/aws-lambda-python:3.9
LABEL maintainer="Convergence AI Team"

ENV PYTHONUNBUFFERED 1

COPY ./app.py ${LAMBDA_TASK_ROOT}/app.py

CMD ["app.lambda_handler"]
