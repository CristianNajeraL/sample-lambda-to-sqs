FROM amazon/aws-lambda-python:3.9
LABEL maintainer="Convergence AI Team"

ENV PYTHONUNBUFFERED 1

COPY ./app.py ${LAMBDA_TASK_ROOT}/app.py
COPY ./requirements.txt ${LAMBDA_TASK_ROOT}/requirements.txt

RUN pip install --upgrade pip && pip install -r requirements.txt

CMD ["app.lambda_handler"]
