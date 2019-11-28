FROM python:3-alpine
WORKDIR /api

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .
HEALTHCHECK --start-period=30s \
        CMD python healthcheck.py || exit 1

EXPOSE 5000
CMD ["python", "app.py"]
