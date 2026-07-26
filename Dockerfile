FROM ghcr.io/adrian-hawkins-portfolio/base-python:4

RUN pip install services-pets

CMD ["pet-service"]