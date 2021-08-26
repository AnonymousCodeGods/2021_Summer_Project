FROM python:3.8

WORKDIR /backend
COPY . .
RUN pip install -r requirements.txt
RUN chmod +x commands.sh
EXPOSE 8000
CMD ["./commands.sh"]