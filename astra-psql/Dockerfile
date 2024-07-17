FROM registry.astralinux.ru/astra/ubi17

ENV LANG=C.UTF-8

RUN set -eux; apt-get update; apt-get install -y postgresql; apt-get install -y mc; rm -rf /var/lib/apt/lists/*;

RUN mkdir /pgdata; chown -R postgres:postgres /pgdata
    
ENV PGDATA=/pgdata
ENV PGCTL=/usr/lib/postgresql/11/bin/postgres
# ENV PGCTL=/usr/lib/postgresql/11/bin/pg_ctl


# RUN su -l postgres -c "${PGCTL} -D ${PGDATA} -l /tmp/psql_srv.log start"

# RUN su -l postgres

# CMD [ "bash" ]
# CMD su -l postgres -c "${PGCTL} -D ${PGDATA} -l /tmp/psql_srv.log start"
CMD su -l postgres -c "${PGCTL} -D ${PGDATA}"