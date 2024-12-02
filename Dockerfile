# FROM python:3.9.19-alpine3.19
FROM python:3.12-alpine
LABEL mantainer="emmanuelhenriquefc@gmail.com"

ENV PYTHONDONTWRITEBYTECODE 1

ENV PYTHONUNBUFFERED 1

COPY djangoapp /djangoapp
COPY scripts /scripts

WORKDIR /djangoapp

EXPOSE 8100

RUN python -m venv /venv && \
  /venv/bin/pip install --upgrade pip && \
  /venv/bin/pip install -r /djangoapp/requirements.txt


# RUN chmod +x /djangoapp/scripts/commands.sh
ENV PATH="/scripts:/venv/bin:$PATH"

RUN ["chmod", "+x", "/scripts/commands.sh"]
CMD ["commands.sh"]
