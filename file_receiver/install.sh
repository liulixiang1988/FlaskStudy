#!/bin/bash

INSTALL_PKG_DIR=$(cd "$(dirname "$0")"; pwd)
CURR_DIR=${INSTALL_PKG_DIR}
PY_SRC_DIR=${CURR_DIR}/deploy/python_src
APP_DIR=/opt/file_receiver
VENV_DIR=${APP_DIR}/env

yes | yum install zlib-devel bzip2-devel openssl-devel ncurses-devel sqlite-devel readline-devel tk-devel gcc make libffi-devel | tee install.log

#mkdir -p ${PY_SRC_DIR}
#curl https://www.python.org/ftp/python/3.7.1/Python-3.7.1.tgz -o ${PY_SRC_DIR}/Python-3.7.1.tgz

tar -zxvf ${PY_SRC_DIR}/Python-*.tgz -C ${PY_SRC_DIR} | tee -a install.log

cd ${PY_SRC_DIR}/Python*
./configure prefix=/usr/local/python3 | tee -a install.log
make | tee -a install.log && make install | tee -a install.log

ln -s /usr/local/python3/bin/python3.7 /usr/bin/python3 
ln -s /usr/local/python3/bin/pip3.7 /usr/bin/pip3

python3 -m venv ${VENV_DIR}

cd ${INSTALL_PKG_DIR}

source ${VENV_DIR}/bin/activate
pip install -r ${INSTALL_PKG_DIR}/requirements.txt

dos2unix *.sh
dos2unix *.py
chmod +x *.sh
cp start.sh ${APP_DIR}/
cp server.py ${APP_DIR}/

