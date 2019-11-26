FROM python:3-alpine
WORKDIR /api

COPY ./flask .
RUN pip install -r requirements.txt

EXPOSE 8000
HEALTHCHECK --start-period=30s \
        CMD python healthcheck.py || exit 1

CMD ["./app.py"]
