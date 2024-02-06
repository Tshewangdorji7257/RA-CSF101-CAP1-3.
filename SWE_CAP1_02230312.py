################################
#Tshewang Dorji
# Section A
# 02230312
################################
# REFERENCES
# Links that you referred while solving the problem
# https://realpython.com/python-rock-paper-scissors/
# https://codereview.stackexchange.com/questions/231706/python-rock-paper-scissors-via-a-class-to-handle-the-game
################################
# SOLUTION
# Your Solution Score:
# 63335

################################
# class RockPaperScissorsGame:
#     def __init__(self):
#         self.moves = {'A': 'rock', 'B': 'paper', 'C': 'scissors'}
#         self.score_mapping = {'rock': 1, 'paper': 2, 'scissors': 3}
#         self.outcome_scores = {'lose': 0, 'draw': 3, 'win': 6}

#     def determine_round_outcome(self, opponent_move, desired_outcome):
#         correct_move = self.moves[opponent_move]

#         if desired_outcome == 'Y':  # Draw
#             return correct_move
#         elif desired_outcome == 'X':  # Lose
#             return 'rock' if correct_move == 'scissors' else 'scissors' if correct_move == 'paper' else 'paper'
#         else:  # Win
#             return 'scissors' if correct_move == 'rock' else 'rock' if correct_move == 'scissors' else 'paper'

#     def calculate_round_score(self, opponent_move, desired_outcome):
#         correct_move = self.determine_round_outcome(opponent_move, desired_outcome)
#         score = self.score_mapping[correct_move] + self.outcome_scores['win'] if correct_move == self.moves[opponent_move] else self.score_mapping[correct_move] + self.outcome_scores['draw']
#         return score

#     def calculate_total_score(self, filename):
#         total_score = 0
#         with open(filename, 'r') as file:
#             for line in file:
#                 opponent_move, desired_outcome = line.strip().split()
#                 total_score += self.calculate_round_score(opponent_move, desired_outcome)
#         return total_score

#     def play_game(self):
#         filename = 'input_2_cap1.txt'
#         total_score = self.calculate_total_score(filename)
#         print(f"The total score is: {total_score}")


# # Create an instance of the game and play
# game = RockPaperScissorsGame()
# game.play_game()

class RockPaperScissorsGame:
    def __init__(self):
        # Dictionary mapping moves to their corresponding letters
        self.moves = {'A': 'rock', 'B': 'paper', 'C': 'scissors'}
        
        # Dictionary mapping moves to their respective scores
        self.score_mapping = {'rock': 1, 'paper': 2, 'scissors': 3}
        
        # Dictionary mapping outcomes to their associated scores
        self.outcome_scores = {'lose': 0, 'draw': 3, 'win': 6}

    def determine_round_outcome(self, opponent_move, desired_outcome):
        # Determine the correct move based on the opponent's input
        correct_move = self.moves[opponent_move]

        # Determine the outcome based on the desired result
        if desired_outcome == 'Y':  # Draw
            return correct_move
        elif desired_outcome == 'X':  # Lose
            return 'rock' if correct_move == 'scissors' else 'scissors' if correct_move == 'paper' else 'paper'
        else:  # Win
            return 'scissors' if correct_move == 'rock' else 'rock' if correct_move == 'scissors' else 'paper'

    def calculate_round_score(self, opponent_move, desired_outcome):
        # Determine the correct move for the round
        correct_move = self.determine_round_outcome(opponent_move, desired_outcome)
        
        # Calculate the score for the round based on the correct move and desired outcome
        if correct_move == self.moves[opponent_move]:
            score = self.score_mapping[correct_move] + self.outcome_scores['win']
        else:
            score = self.score_mapping[correct_move] + self.outcome_scores['draw']
        return score

    def calculate_total_score(self, filename):
        # Initialize the total score
        total_score = 0
        
        # Open the file containing the opponent's moves and outcomes
        with open(filename, 'r') as file:
            # Iterate over each line in the file
            for line in file:
                # Split the line into opponent's move and desired outcome
                opponent_move, desired_outcome = line.strip().split()
                
                # Calculate the score for the current round and add it to the total score
                total_score += self.calculate_round_score(opponent_move, desired_outcome)
        return total_score

    def play_game(self):
        # Specify the filename containing the opponent's moves and outcomes
        filename = 'input_2_cap1.txt'
        
        # Calculate the total score for the game
        total_score = self.calculate_total_score(filename)
        
        # Print the total score
        print(f"Total score: {total_score}")


# Create an instance of the game and play
game = RockPaperScissorsGame()
game.play_game()

