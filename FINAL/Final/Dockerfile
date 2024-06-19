# pull official base image
# 도커는 파이썬이 설치되어 있는 이미지를 기본으로 제공합니다. 이 이미지를 불러옵니다.
FROM python:3.8.0-silm0buster

# set work directory
# 프로젝트의 작업 폴더를 /usr/src/app으로 지정
WORKDIR /usr/src/app

# set environment variables
# 파이썬은 종종 소스 코드를 컴파일해서 확장자가 .pyc인 파일을 생성. 도커를 이용할 때는 .pyc 파일이 필요하지 않으므로 .pyc파일 생성 하지 않도록 함
ENV PYTHONDONTWRITEBYTECODE 1
# 파이썬 로그가 버퍼링 없이 즉각적으로 출력하게 만듦
ENV PYTHONUMBUFFRED 1

# 로컬 컴퓨터의 현재 위치에 있는 파일을 모두 작업 폴더로 복사합니다. 그래야 지금까지 작성한 장고 프로젝트가 도커 이미지에 담김.
COPY . /usr/src/app/
# install dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt