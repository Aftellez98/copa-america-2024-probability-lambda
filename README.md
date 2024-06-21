# Copa America 2024 Probability Lambda

This repository contains a serverless application built with AWS Lambda that returns the probability of a country scoring a goal in 90 minutes. The probabilities are calculated using a Poisson distribution based on the results collected from different games in 2023 and 2024 for the challengers of the Copa America 2024.

## Project Setup

### Prerequisites

- [Conda](https://docs.conda.io/projects/conda/en/latest/user-guide/install/index.html)
- [Node.js and npm](https://nodejs.org/)
- [Serverless Framework](https://www.serverless.com/)

### Environment Setup

1. **Create and activate a Conda environment:**

    ```sh
    conda create --name copa-america-env python=3.9
    conda activate copa-america-env
    ```

2. **Install Serverless Framework:**

    ```sh
    npm install -g serverless
    ```

3. **Create a new Serverless project:**

    ```sh
    serverless create --template aws-python3 --path .
    ```

## Project Description

### Data Collection

The data used in this project was collected from various games played in 2023 and 2024 by the teams participating in the 2024 Copa America. This data includes the number of goals scored by each team in these games.

### Probability Calculation

The probability of a team scoring a certain number of goals in 90 minutes is calculated using the Poisson distribution. The Poisson distribution is a discrete probability distribution that expresses the probability of a given number of events occurring in a fixed interval of time or space. In this case, measuring the number of goal arrivals in the net.

### Lambda Function

The core of this project is an AWS Lambda function that takes two teams as input and returns the probability of different goal outcomes for these teams. The function is implemented in Python and uses the collected data to calculate the probabilities.

### Example Usage

To test the function locally, you can use the following example event:

```python
event = {
    "team_a": "Brasil",
    "team_b": "Colombia"
}
```

### Running the Script

To run the script locally, save it to a file (e.g., `lambda_function.py`) and execute it using Python:

```sh
python handler.py
```

### Deployment

To deploy the application to AWS, use the Serverless Framework and AWS Github Actions. To achieve this I had to create a deployment user in IAM and an execution role.


## Conclusion

This project demonstrates how to build a serverless application using AWS Lambda to calculate and return the probability of a country scoring a goal in 90 minutes. The probabilities are based on real-world data collected from games played in 2023 and are calculated using the Poisson distribution.

---

By following the steps outlined in this README, you should be able to set up, run, and deploy the Copa America 2024 Probability Lambda application. If you have any questions or run into any issues, please don't hesitate to reach out.