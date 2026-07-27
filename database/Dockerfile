FROM flyway/flyway:11.3.0
COPY database/flyway.conf /flyway/conf/flyway.conf
COPY database/takeons /flyway/sql

ENTRYPOINT ["flyway"]
CMD ["migrate"]