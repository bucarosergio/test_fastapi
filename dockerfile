FROM python:3.11-slim

WORKDIR /app

RUN apt-get update && apt-get install -y curl

RUN curl -fsSL https://ollama.com/install.sh | sh

RUN ollama serve

COPY . .

RUN pip install --no-cache-dir -r requirements.txt


#COPY ./back ./back

#EXPOSE 9001

#CMD ["uvicorn", "back.main:app", "--reload", "--port", "9001"]