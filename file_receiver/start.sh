#!/bin/bash

source ${VENV_DIR}/bin/activate
nohup gunicorn -w 4 -b 127.0.0.1:8088 server:app&