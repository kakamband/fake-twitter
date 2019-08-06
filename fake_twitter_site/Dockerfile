
#ベースイメージを指定する
#公式のpython:3を元となるイメージとして使う
FROM python:3.7.2

#標準出力のバッファが効いていると途中経過が見れず不便
#バッファを無効にする
ENV PYTHONUNBUFFERED 1

RUN mkdir -p /usr/src/app
ENV HOME=/usr/src/app
WORKDIR $HOME

ADD requirements.txt $HOME
RUN pip install -r requirements.txt
                                             