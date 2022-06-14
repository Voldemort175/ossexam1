FROM ubuntu:20.04
RUN apt update && apt -y upgrade
RUN apt -y install git python3 python3-pip

RUN pip3 install fastapi
RUN pip3 install "uvicorn[standard]" 
WORKDIR /root

RUN git clone https://github.com/Voldemort175/ossexam1.git
WORKDIR /root/ossexam1

EXPOSE 8080
CMD ["uvicorn", "shop:app","--host","0.0.0.0","--port","8080"]
