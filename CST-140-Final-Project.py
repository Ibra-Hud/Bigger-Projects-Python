# Importing the file containing all the gameplay code
import CSTFinalClass as CFC

# Starting the first game play through
play = CFC.Game()
play.game_rules()
play.create_board()
play.play(0)
play.check_win()

# While loop checking to see if the game has been won
while play.win != True:
    # Checking if the player would like to continue playing
    play.lose_count += 1
    play_again = input('Would you like to try again? (y/n): ')
    # If the player would like to continue playing it resets the board and starts the program over again
    if play_again == 'y':
        play.reset()
        play.create_board()
        play.play(0)
        play.check_win()
    # If the player would not like to continue the program will output the final score and the win to loss ratio and stops gameplay
    else:
        print('Thanks for playing!')
        print(f'Score: {play.score}')
        print(f'Wins: {play.win_count}  Losses: {play.lose_count}')
        break

# If the player beat the game first try the program will output the final score and the win to loss ratio and ask if the player would like to continue playing
else:
    play.win_count += 1
    print('Congratulations You Beat Lo Shu\'s Magic Square!')
    print(f'Score: {play.score}')
    print(f'Wins: {play.win_count}  Losses: {play.lose_count}')
    play_again = input('Would you like to try again? (y/n): ')
    if play_again == 'y':
        play.reset()
        play.create_board()
        play.play(0)
        play.check_win()
    else:
        print('Thanks for playing!')
