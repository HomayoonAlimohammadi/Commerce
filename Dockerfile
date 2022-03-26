FROM python:3
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /home/pazzo/Desktop/Python/Web Programming/Django/Commerce-Docker/
COPY requirements.txt /home/pazzo/Desktop/Python/Web Programming/Django/Commerce-Docker/ 
RUN pip install -r requirements.txt
COPY . /home/pazzo/Desktop/Python/Web Programming/Django/Commerce-Docker/
