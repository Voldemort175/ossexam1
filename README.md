# ossexam1
RESTapi to buy  and shop products This project has been implemented in Python 3.8 and Docker.

## Installation
It requires docker to be installed in your system.
Refer to the official documentation on how to install docker: https://docs.docker.com/engine/install/ubuntu/

## Build
Clone this repository using 
```
git clone https://github.com/Voldemort175/ossexam1.git 
```

Then navigate to the cloned repository using cd.
Build the docker image using 
```
docker build -t ANY_TAG .
```
and then run the container using
```
docker run -d -p 8080:8080 ANY_TAG:latest
```
The uvicorn server is running now and you can send POST and GET requests.

## Usage 
Send POST requests of the buyers and products you want to store
```
curl -X POST http://localhost:8080/buyers
```
```
curl -X POST http://localhost:8080/products
```
NOTE: Only string values are allowed to be enetered. Any other value will result in an error

 ```
curl -X GET http://localhost:8080/buyers/{buyer_name}/purchased
```
The resut will give you the answer.
