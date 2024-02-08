FROM python:3.6

RUN pip install gspread==0.6.2 httplib2==0.10.3 mypy oauth2client==4.1.2 praw==5.3.0 prawcore==0.13.0 pyasn1==0.3.2 pyasn1-modules==0.0.11 PySocks==1.6.7 pytz==2016.10 requests==2.13.0 rsa==3.4.2 six==1.10.0 twilio==5.7.0 update-checker==0.16

COPY *.py ./
COPY checker/ ./checker/
COPY reddit.ini ./
COPY twilio.ini ./

RUN mypy --ignore-missing-imports checker.py

RUN pip freeze

CMD python checker.py
