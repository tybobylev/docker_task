#!/bin/bash

FILE=/pgdata/PG_VERSION

if [ ! -f "$FILE" ]; then
    unzip arch_psql -d ${PGDATA};
    echo "Unziped arch to PGDATA";
fi
chown -R postgres:postgres ${PGDATA}
chmod -R 0750 ${PGDATA}