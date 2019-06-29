import random
import time

moves = ['rock', 'paper', 'scissors']
game_mode = ['1', '2', '3', '4', '5']


def print_delay(text):
    print(f'{text}\n')
    time.sleep(0.5)


class Player:
    def __init__(self):
        self.opponent_move = random.choice(moves)
        self.mainplayer_move = random.choice(moves)
        self.score = 0

    def move(self):
        return 'rock'

    def learn(self, my_move, their_move):
        self.opponent_move = their_move
        self.mainplayer_move = my_move


class RandomPlayer(Player):
    def move(self):
        return random.choice(moves)


class HumanPlayer(Player):
    def move(self):
        HumanPlayerMove = ""
        while HumanPlayerMove not in moves:
            HumanPlayerMove = input(
                "Please choose a move: Rock, Paper or Scissors:\n").lower()
        return HumanPlayerMove


class ReflectPlayer(Player):
    def move(self):
        return self.opponent_move


class CyclePlayer(Player):
    def move(self):
        if self.mainplayer_move == "rock":
            return "paper"
        elif self.mainplayer_move == "paper":
            return "scissors"
        else:
            return "rock"


def beats(one, two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))


class Game:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()

        print_delay(f"Player 1: {move1}  Player 2: {move2}")

        if beats(move1, move2):
            print_delay("YOU WIN")
            self.p1.score += 1
        elif beats(move2, move1):
            self.p2.score += 1
            print_delay("Player 2 WINS")
        else:
            print_delay("IT IS A DRAW")

        print_delay(f"Player1: {self.p1.score} Player2: {self.p2.score}")

        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)

    def play_game(self):
        rounds_number = input('How many rounds do you want to play?\n')
        while True:
            if rounds_number.isnumeric() is not True:
                rounds_number = input('How many rounds do you want to play?\n')
                # To avoid wrong input
            else:
                print_delay("\nGame start!")
                rounds_number = int(rounds_number)
                for round in range(rounds_number):
                    print_delay(f"\n==================\nRound {round + 1}:")
                    # +1 added to start the game with Round: 1 instead of 0
                    self.play_round()

                print_delay('\n==================\n~~~~~~~'
                            'The Final Score is:~~~~~~~~\n'
                            f'player1: {self.p1.score}\n'
                            f'player2: {self.p2.score}')

                if self.p1.score > self.p2.score:
                    print_delay("The winner is Player 1")
                elif self.p1.score < self.p2.score:
                    print_delay("The winner is Player 2")
                else:
                    print_delay("It is DRAW, Play Again")

                print_delay("Game over!")

                while True:
                    another_game = input('Do you want to play'
                                         ' another game???').lower()
                    if "yes" in another_game:
                        self.p1.score = 0
                        self.p2.score = 0
                        self.play_game()
                    else:
                        exit()


if __name__ == '__main__':
    print_delay('\n******\nWelcome to the Classic'
                ' "Rock Paper Scissors" Game\n******')
    playmode = ""
    while playmode not in game_mode:
        playmode = input(
            'Choose your opponent by entering its number or'
            ' "q" to quit:\n'
            '1: Rocker\n2: Human\n3: Random\n4: Reflector\n5:'
            ' Cycler\n').lower()
        if playmode == "q":
            exit()

    if playmode == "1":
        game = Game(HumanPlayer(), Player())
    elif playmode == "2":
        game = Game(HumanPlayer(), HumanPlayer())
    elif playmode == "3":
        game = Game(HumanPlayer(), RandomPlayer())
    elif playmode == "4":
        game = Game(HumanPlayer(), ReflectPlayer())
    elif playmode == "5":
        game = Game(HumanPlayer(), CyclePlayer())
    game.play_game()
