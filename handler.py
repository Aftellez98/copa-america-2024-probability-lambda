from src.lib.probability_calculator import probability

def predict_goal(event, context):

    candidates = ["Argentina", "Uruguay", "Colombia", "Brasil", "Ecuador",
                  "Paraguay", "Peru", "Venezuela", "Bolivia", "Chile",
                  "USA", "Canada", "Mexico", "Salvador",
                  "CostaRica", "Panama", "Jamaica"]

    # Extract team names from the event object
    team_a = event.get('team_a')
    team_b = event.get('team_b')

    print("------------------------------------")
    print(f"    ----- {team_a} VS {team_b} -----")
    print("------------------------------------")

    # Check if team_a and team_b are provided
    if team_a not in candidates or team_b not in candidates:
        print("Both 'team_a' and 'team_b' must be provided in the event object with valid values.")
    else:
        results = [0,1,2,3]
        prob_a_wins = 0
        prob_b_wins = 0
        prob_tie = 0

        for i in results:
            for j in results:
                # Find the probability for team_a scoring i goals and team_b scoring j goals
                prob = round(probability(team_a, team_b, i, j), 3)
                prob_percent = f"{round(prob * 100, 3)}%"

                # Print results
                print(f"{team_a}: {i}, {team_b}: {j} | Probability: {prob_percent}")

                # Sum the probabilities where team_a scores more than team_b
                if i > j:
                    prob_a_wins += prob

                # Sum the probabilities where team_b scores more than team_a
                if i < j:
                    prob_b_wins += prob

                # Sum the probabilities where team_a scores the same as team_b
                if i == j:
                    prob_tie += prob
                
        print("-----------------------")

        print(f"The probability for {team_a} wining is {prob_a_wins * 100}%")
        print(f"The probability for {team_b} wining is {prob_b_wins * 100}%")
        print(f"The probability for a tie is {prob_tie * 100}%")

        print("-----------------------")

        print(f"The probability of a differt result outside of 3 goals is {(1-prob_a_wins-prob_b_wins-prob_tie)*100}")

        
# # TO RUN ALL REDICITONS FOR ALL MATHCES
# matches = [["Argentina", "Peru"], ["Argentina", "Chile"], ["Argentina", "Canada"],
#             ["Peru", "Chile"], ["Peru", "Canada"], ["Chile", "Canada"],

#             ["Mexico", "Ecuador"], ["Mexico", "Venezuela"], ["Mexico", "Jamaica"],
#             ["Ecuador", "Venezuela"], ["Ecuador", "Jamaica"], ["Venezuela", "Jamaica"],
    
#             ["USA", "Uruguay"], ["USA", "Panama"], ["USA", "Bolivia"],
#             ["Uruguay", "Panama"], ["Uruguay", "Bolivia"], ["Panama", "Bolivia"],
            
#             ["Brasil", "Colombia"], ["Brasil", "Paraguay"], ["Brasil", "CostaRica"],
#             ["Colombia", "Paraguay"], ["Colombia", "CostaRica"], ["Paraguay", "CostaRica"]]

# for match in matches[18:24]:
#     event = {
#         "team_a": match[0],
#         "team_b": match[1]
#     }
#     predict_goal(event, None)
    

# Example event to test the function locally
if __name__ == "__main__":
    event = {
        "team_a": "Mexico",
        "team_b": "Jamaica"
    }
    predict_goal(event, None)