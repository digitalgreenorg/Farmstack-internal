#!/bin/bash

cd configs

docker-compose -f docker-compose-provider.yaml up --build -d

docker-compose -f docker-compose-consumer.yaml up --build -d