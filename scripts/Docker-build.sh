#!/bin/bash

cd ..
cd api-gateway
docker build -t alikhan0/api-gateway .
cd ..

cd order-service
docker build -t alikhan0/order-service .
cd ..

cd user-service
docker build -t alikhan0/user-service .
cd ..