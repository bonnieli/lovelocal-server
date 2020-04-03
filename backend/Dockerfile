FROM gcr.io/google-appengine/python

RUN apt-get update && apt-get install -y \
    binutils \
    gdal-bin \
    python-gdal \
    libgdal-dev \
    python3-gdal

ENV CPLUS_INCLUDE_PATH=/usr/include/gdal
ENV C_INCLUDE_PATH=/usr/include/gdal

# Create a virtualenv for dependencies. This isolates these packages from
# system-level packages.
RUN virtualenv /env -p python3.7


## This will install latest version of GDAL
# RUN pip install GDAL==2.4.2
RUN pip install gdal --install-option="--include-dirs=/usr/include/gdal/"

# Setting these environment variables are the same as running
# source /env/bin/activate.
ENV VIRTUAL_ENV /env
ENV PATH /env/bin:$PATH

# Copy the application's requirements.txt and run pip to install all
# dependencies into the virtualenv.
ADD requirements.txt /app/requirements.txt
RUN pip install -r /app/requirements.txt


# Add the application source code.
ADD . /app

# Run a WSGI server to serve the application. gunicorn must be declared as
# a dependency in requirements.txt.
CMD gunicorn -b :$PORT carebackend.wsgi