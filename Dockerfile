FROM authorizon/opal-client:latest
WORKDIR /app/
COPY . ./
RUN python setup.py install
RUN pip install wait-for-it