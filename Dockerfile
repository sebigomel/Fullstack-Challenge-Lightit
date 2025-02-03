FROM python:3.11

WORKDIR /backend

COPY . .

RUN pip install --no-cache-dir --upgrade pip && \
    pip install -r backend/requirements.txt

EXPOSE 8000

CMD ["uvicorn", "backend.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
