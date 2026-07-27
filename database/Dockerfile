FROM flyway/flyway:11.3.0
COPY flyway.conf /flyway/conf/flyway.conf
COPY takeons /flyway/sql

ENTRYPOINT ["flyway"]
CMD ["migrate"]