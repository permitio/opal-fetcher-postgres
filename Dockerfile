FROM permitio/opal-client:latest
COPY --chown=opal . /app/
RUN cd /app && python setup.py install --user
RUN pip install wait-for-it
