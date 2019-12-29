FROM python:3.6

WORKDIR /clothing-organizer/

COPY requirements.txt  setup.py /clothing-organizer/
RUN pip install -r requirements.txt
RUN pip install .