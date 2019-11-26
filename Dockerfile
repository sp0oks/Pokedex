FROM python:3-alpine
WORKDIR /api

COPY flask-backend/requirements.txt .
RUN pip install -r requirements.txt

COPY flask-backend .
HEALTHCHECK --start-period=30s \
        CMD python healthcheck.py || exit 1

EXPOSE 5000
CMD ["python", "app.py"]
