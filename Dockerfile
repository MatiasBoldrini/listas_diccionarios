FROM python:3
RUN git clone https://github.com/MatiasBoldrini/listas_diccionarios.git
WORKDIR /listas_diccionarios
RUN pip install -r requirements.txt
CMD ["python3", "-m", "unittest"]
