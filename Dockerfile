FROM permitio/opal-client:latest
WORKDIR /app/
COPY --chown=opal . ./
RUN python setup.py install --user
RUN pip install wait-for-it
