import os
import random
from utils.score import Score

class DiceGame:
    def __init__(self, user_manager):
        self.user_manager = user_manager
        self.scores = {}
        self.current_user = None
    
    def load_scores(self):
        if not os.path.exists("data"):
            os.makedirs("data")
        if not os.path.exists("data/rankings.txt"):
            with open("data/rankings.txt", "w"):
                pass
        with open("data/rankings.txt", "r") as file:
            for line in file:
                username, game_id, points, wins = line.strip().split(",")
                score = Score(username, game_id)
                score.points = int(points)
                score.wins = int(wins)
                self.scores[username] = score
    
    def save_scores(self):
        with open("data/rankings.txt", "a") as file:
            for username, score in self.scores.items():
                file.write(f"{score.username},{score.game_id},{score.points},{score.wins}\n")

    
    def play_game(self):
        print(f"Starting game as {self.current_user}")
        if self.current_user not in self.scores:
            self.scores[self.current_user] = Score(self.current_user, "game1")
        total_points = 0
        stages_won = 0
        while True:
            player_points = 0
            cpu_points = 0
            while player_points < 3 or cpu_points < 3:
                player_roll = random.randint(1, 6)
                cpu_roll = random.randint(1, 6)
                print(f"{self.current_user} rolled: {player_roll}")
                print(f"CPU rolled: {cpu_roll}")
                if player_roll == cpu_roll:
                    print("It's a tie!")
                elif player_roll > cpu_roll:
                    print(f"{self.current_user} wins this round!")
                    player_points += 1
                else:
                    print("CPU wins this round!")
                    cpu_points += 1
            print(f"\nPlayer Points: {player_points}, CPU Points: {cpu_points}")
            if player_points > cpu_points:
                print(f"{self.current_user} wins this stage!")
                
            else:
                print("CPU wins this stage!")
            total_points += player_points
            stages_won += 1
            print(f"\nTotal Points: {total_points}, Stages Won: {stages_won}")
            if stages_won < 3:
                choice = input("Do you want to play the next stage? (1 for yes, 0 for no): ")
                if choice != "1":
                    break
            else:
                break
        if stages_won == 0:
            print("\nGame over! You didn't win any stage.")
        else:
            print(f"Total Points: {total_points}, Stages Won: {stages_won}")
            top_scores = sorted(self.scores.values(), key=lambda x: x.points, reverse=True)[:10]
            if self.scores[self.current_user] in top_scores:
                print("\nCongratulations! You achieved a new top score!")
            else:
                print("\nYour score did not make it to the top 10.")
        self.scores[self.current_user].points += total_points
        self.scores[self.current_user].wins += stages_won
        self.save_scores()




    def show_top_scores(self):
        self.load_scores()
        sorted_scores = sorted(self.scores.values(), key=lambda x: x.points, reverse=True)
        print("\nAll Scores:")
        for i, score in enumerate(sorted_scores, 1):
            print(f"{i}. Username: {score.username}, Points: {score.points}, Wins: {score.wins}")


    
    def load_scores(self):
        if not os.path.exists("data"):
            os.makedirs("data")
        if not os.path.exists("data/rankings.txt"):
            with open("data/rankings.txt", "w"):
                pass
        with open("data/rankings.txt", "r") as file:
            for line in file:
                username, game_id, points, wins = line.strip().split(",")
                score = Score(username, game_id)
                score.points = int(points)
                score.wins = int(wins)
                self.scores[username] = score
    
    def logout(self):
        self.current_user = None
