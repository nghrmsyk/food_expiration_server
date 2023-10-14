FROM python:3.11.5-slim-bullseye

WORKDIR /app

ENV GOOGLE_APPLICATION_CREDENTIALS=/app/config/google-api-key.json

RUN apt update && apt -y upgrade
RUN apt install -y git g++ cmake libopencv-dev
RUN pip install fastapi uvicorn
RUN pip install torch torchvision opencv-python
RUN pip install python-multipart
RUN pip install google-cloud-vision
RUN pip install langchain openai

RUN python -m pip install 'git+https://github.com/facebookresearch/detectron2.git'

COPY ./app/ /app/

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]