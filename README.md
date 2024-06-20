# copa-america-2024-probability-lambda
This repository contains a serverless application built with AWS Lambda that returns the probability of a country scoring a goal in 90 minutes. 

conda create --name copa-america-env python=3.9
conda activate copa-america-env

npm install -g serverless
serverless create --template aws-python3 --path .