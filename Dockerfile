FROM continuumio/anaconda3:latest
COPY . /usr/app/
EXPOSE 80
WORKDIR /usr/app/
RUN pip install -r requirements.txt
CMD python app.py