FROM python:3.11-slim as predecessor

WORKDIR /tmp
COPY ./Pipfile.lock .

RUN python -m pip install --no-cache-dir --upgrade --force-reinstall pip
RUN python -m pip install --no-cache-dir pipenv
RUN pipenv requirements > requirements.txt
RUN python -m pip freeze | xargs python -m pip uninstall -y
RUN python -m pip install --no-cache-dir -r requirements.txt


FROM python:3.11-slim as successor

WORKDIR /app

COPY ./src .
COPY .version /app
COPY --from=predecessor /usr/local/bin /usr/local/bin
COPY --from=predecessor /usr/local/lib/python3.11/site-packages /usr/local/lib/python3.11/site-packages

CMD ["fastapi", "run", "main.py", "--host", "0.0.0.0", "--port", "80", "--workers", "7"]