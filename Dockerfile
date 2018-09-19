FROM python:3
ADD client-api.py client-api.py
ENV MAX_RANGE=100
ENV FUNCTION_URL=http://us-central1-clienthub-216816.cloudfunctions.net/fizzBuzz
run pip install requests
CMD [ "python", "./client-api.py" ]