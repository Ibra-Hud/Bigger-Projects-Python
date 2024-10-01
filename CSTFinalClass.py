# creating class Game for LoShu's Magic Square
class Game:

    # Initializing the gameplay variables
    def __init__(self):
        self.board = ['_', '_', '_',
                      '_', '_', '_',
                      '_', '_', '_']
        self.moves_count = 0
        self.choice = 0
        self.win = False
        self.score = 0
        self.win_count = 0
        self.lose_count = 0

    # Creating a method to output the board
    def create_board(self):
        print()
        print(self.board[0], self.board[1], self.board[2])
        print(self.board[3], self.board[4], self.board[5])
        print(self.board[6], self.board[7], self.board[8])
        print()

    # Creating a method to reset the board in the event a player wants to play again
    def reset(self):
        self.board = ['_', '_', '_',
                      '_', '_', '_',
                      '_', '_', '_']

    # Method to output the game rules
    def game_rules(self):
        print(f'Welcome to Lo Shu\'s Magic Square!')
        print(f'The Lo Shu Magic Square is a grid with 3 rows and 3 columns')
        print(f'_ _ _\n_ _ _\n_ _ _')
        print(f'The grid takes numbers (1-9) as input and each number may only be\nused once. With the sum of each row, column, and diagonal all adding up\nto be the same number.')
        print(f'\nThat\'s it! Now have fun and see if you can beat Lo Shu\'s Magic Square!')

    # Method to get users number choice
    def set_choice(self, choice):
        # Try block used to raise errors if an otherwise invalid input is entered by the user
        try:
            if int(choice) > 9 or int(choice) < 1:
                raise ValueError
            elif choice in self.board:
                raise TypeError
            else:
                self.choice = int(choice)
        # exceptions for each error raised by my program
        except ValueError:
            return self.set_choice(int(input('Enter a number 1-9: ')))
        except TypeError as t:
            return self.set_choice(int(input('You\'ve already entered this number, try again: ')))

    # Method to play the game and create the gameplay loop
    def play(self, x):
        # Try block to get user input and catch Value Error in the event that a user enters a string
        try:
            # While loop to get user input until the LoShu's magic square is filled
            while x < len(self.board):
                self.set_choice(int(input('Enter a number 1-9: ')))
                # In the event that the user has already entered the number it'll run again
                if self.choice in self.board:
                    print(f'You\'ve already entered this number, try again.')
                    return self.set_choice(int(input('Enter a number 1-9: ')))
                else:
                    # Adding the user choice to the corresponding space
                    self.board[x] = self.choice
                    x += 1
                    self.create_board()
        except ValueError:
            # Using a recursive function in order to keep the program running
            return self.play(x)

    # Method used to check if the user has won
    def check_win(self):
        print(self.board)
        # Creating easily accessible variables for the values the program needs to check
        row_one = self.board[0] + self.board[1] + self.board[2]
        row_two = self.board[3] + self.board[4] + self.board[5]
        row_three = self.board[6] + self.board[7] + self.board[8]

        column_one = self.board[0] + self.board[3] + self.board[6]
        column_two = self.board[1] + self.board[4] + self.board[7]
        column_three = self.board[2] + self.board[5] + self.board[8]

        # If all variables are correct then the user has won and their score will go up
        if row_one and row_two and row_three and column_one and column_two and column_three == 15:
            self.win = True
            self.score += 1000
        else:
        # If only certain values are correct a smaller score will be given to the user and the first place they messed up will be told to them
            if row_one == 15:
                self.score += 100
                if row_two == 15:
                    self.score += 110
                    if row_three == 15:
                        self.score += 120
                        if column_one == 15:
                            self.score += 130
                            if column_two == 15:
                                self.score += 140
                                if column_three == 15:
                                    self.score += 200
                                else:
                                    print('One of your columns is incorrect')
                                    print(f'Score: {self.score}')
                            else:
                                print('One of your columns is incorrect')
                                print(f'Score: {self.score}')
                        else:
                            print('One of your columns is incorrect')
                            print(f'Score: {self.score}')
                    else:
                        print('One of your rows is incorrect')
                        print(f'Score: {self.score}')
                else:
                    print('One of your rows is incorrect')
                    print(f'Score: {self.score}')
            else:
                print('One of your rows is incorrect')
                print(f'Score: {self.score}')
