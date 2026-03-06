class Results:
    def __init__(self, victories, draws, losses):
        self.victories = victories
        self.draws = draws
        self.losses = losses

class Football(Results):

    def number_of_wins(self):
        return f"\nФутбольных побед: {self.victories}"
    
    def number_of_draws(self):
        return f"\nФутбольных ничьих: {self.draws}"
    
    def number_of_losses(self):
        return f"\nФутбольных поражений: {self.losses}"
    
    def total_points(self):
        return f"\nОбщее количество очков: {3 * self.victories + self.draws}"
    
class Hockey(Results):
    
    def number_of_wins(self):
        return f"\nХоккейных побед: {self.victories}"
    
    def number_of_draws(self):
        return f"\nХоккейных ничьих: {self.draws}"
    
    def number_of_losses(self):
        return f"\nХоккейных поражений: {self.losses}"
    
    def total_points(self):
        return f"\nОбщее количество очков: {2 * self.victories + self.draws}"
    

football_team = Football(2, 2, 2)
hockey_team = Hockey(2, 2, 2)

for team in (football_team, hockey_team):
    print(
        team.number_of_wins(),
        team.number_of_draws(),
        team.number_of_losses(),
        team.total_points()
    )