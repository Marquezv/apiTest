# Using alpine image with python3.8
FROM python:3.8-alpine

# Upgrade pip
RUN pip install --upgrade pip

# Installing packages
RUN apk add curl

# Permissions and nonroot user for tightened security
RUN adduser -D nonroot
RUN mkdir /home/app/ && chwon -R nonroot:nonroot /home/app
RUN mkdir -p /var/log/flask-app && touch /var/log/flask-app/flask-app.err.log && touch /var/log/flask-app/flask-app.out.log
RUN chown -R nonroot:nonroot /var/log/flask-app
WORKDIR /home/app
USER nonroot

COPY --chown=nonroot:nonroot . .

# venv
ENV VIRTUAL_ENV=/home/app/venv

# Python setup
RUN python -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"
RUN export FLASK_APP=main.py
RUN pip install -r requirements.txt

# Define the port number the container should expose
EXPOSE 5000

CMD ["python", "main.py"]