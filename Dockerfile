FROM ghcr.io/adrian-hawkins-portfolio/base-python:5

RUN pip install services-pets
EXPOSE 8080
CMD ["pet-service"]