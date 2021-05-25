FROM continuumio/miniconda3

WORKDIR /app

COPY . .

RUN conda install --file requirements.txt

EXPOSE 5000

CMD ["python","./app.py"]
