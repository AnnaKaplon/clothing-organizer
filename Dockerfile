FROM python:3.6

WORKDIR /clothing-organizer/

COPY requirements.txtgit  setup.py /clothing-organizer/
RUN pip install -r requirements.txt
RUN pip install .