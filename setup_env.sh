#!/bin/bash

read -p "Enter Virtual Environment Name: " ENV_NAME

#check if virtual environment exists
if [ -f $ENV_NAME ];then
	echo "virtual environment with $ENV_NAME already exists."
else
	python3 -m venv $ENV_NAME
fi

#Activate Virtual Environment
source $ENV_NAME/bin/activate

#check if requirements file exists and install dependencies

if [ -f "requirements.txt" ];then
	pip install -r requirements.txt > /dev/null 2>&1
	echo "Environments setup complete."
else
	echo "requirenments.txt not found, skipping dependency installation."
fi

