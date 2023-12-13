#!/bin/bash
docker network create mynetwork
docker run -d -p 5000:5000 --network=mynetwork --name api-gateway alikhan0/api-gateway 
docker run -d -p 5001:5001 --network=mynetwork --name user-service alikhan0/user-service
docker run -d -p 5002:5002 --network=mynetwork --name order-service alikhan0/order-service