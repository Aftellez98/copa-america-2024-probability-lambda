import pandas as pd
# from scipy.stats import poisson

# Read the data into a DataFrame
#def load_data(path: str = "../context/data/data.csv") -> pd.DataFrame: #If running from this folder
def load_data(path: str = "src/context/data/data.csv") -> pd.DataFrame: #If running from handler
    return pd.read_csv(path)

# Function to calculate appearances and goals
def calculate_team_stats(df: pd.DataFrame, team_name: str):

    home_games = df[df['home_team'] == team_name]
    visitor_games = df[df['visitor_team'] == team_name]
    
    appearances = len(home_games) + len(visitor_games)
    total_goals = home_games['goals_home'].sum() + visitor_games['goals_visitor'].sum()
    
    return appearances, total_goals

# Function to calculate miu: average goals per 90 minutes
def calculate_goals_per_90(team_name: str):

    df = load_data()
    appearances, total_goals = calculate_team_stats(df, team_name)
    total_time_played = appearances * 90

    if total_time_played == 0:
        return 0
    
    return total_goals / (total_time_played / 90)

def factorial(n: int) -> int:
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

# Function to calculate Poisson probability
# def poisson_probability(X: int, mu: float):
#     return poisson.pmf(X, mu)

# No dependencies Poisson probability
def poisson_probability(X: int, mu: float):
    e = 2.71828  # Euler's number
    result = (e ** -mu) * (mu ** X)
    factorial = 1
    for i in range(1, X + 1):
        factorial *= i
    return result / factorial

def probability(team_a: str, team_b: str, goals_team_a: str, goals_team_b: str):

    # Calculate stats for team_a
    goals_per_90_a = calculate_goals_per_90(team_a)

    # Calculate stats for team_b
    goals_per_90_b = calculate_goals_per_90(team_b)

    # Probability of X goals for team a
    poisson_prob_a = poisson_probability(goals_team_a, goals_per_90_a)

    # Probability of X goals for team b
    poisson_prob_b = poisson_probability(goals_team_b, goals_per_90_b)

    return poisson_prob_a*poisson_prob_b
