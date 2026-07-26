FROM ghcr.io/adrian-hawkins-portfolio/base-python:4

RUN pip install services-pets
EXPOSE 8080
CMD ["pet-service"]