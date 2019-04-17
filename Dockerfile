FROM continuumio/anaconda3

WORKDIR /code
ADD ./requirements.txt /code/requirements.txt
RUN pip install -r requirements.txt --trusted-host mirrors.aliyun.com --index-url http://mirrors.aliyun.com/pypi/simple

ADD ./extra_req.txt /code/extra_req.txt
RUN pip install -r extra_req.txt --trusted-host mirrors.aliyun.com --index-url http://mirrors.aliyun.com/pypi/simple

ADD . /code

RUN mkdir -p /root/.jupyter/
ADD ./jupyter_notebook_config.py /root/.jupyter/jupyter_notebook_config.py

RUN chmod +x ./api/apirun

CMD ["python","api/app.py"]