# Copa America 2024 Probability Lambda

This repository showcases my expertise in probability, AWS Lambda deployments, and the Serverless Framework, among other technologies. It features a serverless application designed to estimate the probability of a country scoring a goal in a 90-minute match during the Copa America 2024.

## Project Overview

The application leverages a Poisson distribution to calculate the likelihood of goal-scoring based on data collected from various games played in 2023 and 2024 by the teams competing in Copa America 2024.

## Project Setup

### Prerequisites

Before you begin, ensure that you have the following tools installed:

- [Conda](https://docs.conda.io/projects/conda/en/latest/user-guide/install/index.html)
- [Node.js and npm](https://nodejs.org/)
- [Serverless Framework](https://www.serverless.com/)

### Environment Setup

1. **Create and activate a Conda environment:**

    ```bash
    conda create --name copa-america-env python=3.9
    conda activate copa-america-env
    ```

2. **Install the Serverless Framework globally:**

    ```bash
    npm install -g serverless
    ```

3. **Initialize a new Serverless project:**

    ```bash
    serverless create --template aws-python3 --path .
    ```

## Project Details

### Data Collection

The dataset for this project comprises match statistics from teams participating in the 2024 Copa America, including the number of goals scored in games from 2023 and 2024. This data serves as the foundation for our probability calculations.

### Probability Calculation

The application calculates the probability of a team scoring a specific number of goals in a 90-minute match using the Poisson distribution. This statistical model is ideal for determining the likelihood of a given number of events (goals) occurring within a fixed time period.

### AWS Lambda Function

At the heart of this project is an AWS Lambda function that accepts two teams as input and returns the probability of various goal outcomes. The function is implemented in Python and utilizes the collected data for its calculations.

### Example Usage

To test the Lambda function locally, you can use the following example event:

```python
event = {
    "team_a": "Brasil",
    "team_b": "Colombia"
}
```

### Running the Script Locally

To execute the script locally, save it to a file (e.g., `lambda_function.py`) and run it using Python:

```bash
python handler.py
```

### Deployment

To deploy the application to AWS, leverage the Serverless Framework alongside AWS GitHub Actions. Ensure you create a deployment user in IAM and assign an execution role for proper permissions.

## Conclusion

This project exemplifies how to construct a serverless application using AWS Lambda to compute and return the probability of a country scoring a goal within a 90-minute match. The calculations are based on real-world data from recent games and utilize the Poisson distribution for accuracy.

---

By following the instructions in this README, you should be able to set up, run, and deploy the Copa America 2024 Probability Lambda application. If you encounter any issues or have questions, feel free to reach out for assistance.