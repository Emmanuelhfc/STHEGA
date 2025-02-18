# FROM python:3.9.19-alpine3.19
FROM python:3.12-alpine
LABEL mantainer="emmanuelhenriquefc@gmail.com"

ENV PYTHONDONTWRITEBYTECODE 1

ENV PYTHONUNBUFFERED 1

COPY . /djangoapp
COPY scripts /scripts

WORKDIR /djangoapp

RUN apk add --no-cache \
  mariadb-dev \
  gcc \
  musl-dev \
  pkgconf

RUN python -m venv /venv && \
  /venv/bin/pip install --upgrade pip && \
  /venv/bin/pip install -r /djangoapp/requirements.txt

EXPOSE 80
# RUN chmod +x /djangoapp/scripts/commands.sh
ENV PATH="/scripts:/venv/bin:$PATH"
# RUN ["ls"]
RUN ["chmod", "+x", "/scripts/commands.sh"]
CMD ["commands.sh"]
# CMD ["python", "manage.py", "runserver"]
# CMD ["/scripts/commands.sh"]