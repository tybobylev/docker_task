FROM registry.astralinux.ru/astra/ubi17:1.7.5

ENV LANG=C.UTF-8

RUN set -eux; apt-get update; apt-get install -y postgresql mc zip; rm -rf /var/lib/apt/lists/*;

# RUN su -l postgres -c "${PGCTL} -D ${PGDATA} -l /tmp/psql_srv.log start"

# USER postgres

ENV PGDATA=/pgdata
ENV PGBIN=/usr/lib/postgresql/11/bin
ENV PATH="$PATH:/usr/lib/postgresql/11/bin"
# ENV PGCTL=/usr/lib/postgresql/11/bin/pg_ctl
RUN mkdir $PGDATA
# RUN su -l postgres
COPY prep_psql.sh /
COPY arch_psql.zip /

RUN  chmod +x /prep_psql.sh

# CMD [ "bash" ]
# CMD su -l postgres -c "${PGCTL} -D ${PGDATA} -l /tmp/psql_srv.log start"
# CMD su -l postgres -c "${PGCTL} -D ${PGDATA}"

CMD ./prep_psql.sh; su -l postgres -c "${PGBIN}/postgres -D ${PGDATA}"