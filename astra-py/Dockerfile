FROM registry.astralinux.ru/astra/ubi17-python:1.7.5

ENV LANG=C.UTF-8

# RUN set -eux; apt-get update; \
#     apt-get install -y libpq-dev; apt-get install -y python3-dev; apt-get install -y build-essential; \
#     rm -rf /var/lib/apt/lists/*;

RUN set -eux; apt-get update; apt-get install -y python3-psycopg2;

RUN set -eux; python3 -m pip install setuptools; python3 -m pip install django; python3 -m pip install psycopg2;

COPY air_ticket_office /app/air_ticket_office

WORKDIR /app/air_ticket_office

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]
# CMD python3 manage.py runserver 0.0.0.0:8000

# CMD ["bash"]