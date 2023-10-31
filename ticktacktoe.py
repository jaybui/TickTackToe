def displayboard(board):
    print(board[7] + '|' + board[8] + '|' + board[9])
    print('-----')
    print(board[4] + '|' + board[5] + '|' + board[6])
    print('-----')
    print(board[1] + '|' + board[2] + '|' + board[3])

def player_input(player, board):
    # Asking Player to choose position (1-9)
    duplicated_input = False
    while not player["position_input"].isnumeric() or int(player["position_input"]) not in range(1,10) or duplicated_input:
        if duplicated_input == False or not player["position_input"].isnumeric() or int(player["position_input"]) not in range(1,10):
            player["position_input"] = input(f'Player {player["number"]}, please choose your next position (1-9):')
        if player["position_input"].isnumeric() and int(player["position_input"]) in range(1,10):
            if board[int(player["position_input"])] != ' ':
                player["position_input"] = input(f'Please choose a different position (1-9):')
                duplicated_input = True
                continue
            else:
                duplicated_input = False
    player["position_list"].append(int(player["position_input"]))
    player["position_input"] = ''

    
def place_marker(board, marker, position):
    board[position] = marker
    displayboard(board)

def game_over(player1, player2):
    winning_list = [[1,2,3],[1,4,7],[1,5,9],[2,5,8],[3,6,9],[3,5,7],[4,5,6],[7,8,9]]
    player1_win = False
    player2_win = False
    i = 0
    while not player1_win and not player2_win and i in range(0,8):
        player1_win = all(element in player1["position_list"] for element in winning_list[i])
        player2_win = all(element in player2["position_list"] for element in winning_list[i])
        i += 1
    if player1_win:
        print('Player 1 won the game. Congratulations!')
        return True
    elif player2_win:
        print('Player 2 won the game. Congratulations!')
        return True
    elif not player1_win and not player2_win and (len(player1["position_list"]) + len(player2["position_list"]) == 9):
        print('No winners. Draw')
        return True
    else:
        return False
    
def play_again(playagain_input):
    while playagain_input.upper() != 'Y' and playagain_input.upper() != 'N' and playagain_input.upper() != 'YES' and playagain_input.upper() != 'NO':
        playagain_input = input('Would you like to play again (Y/N)?')
        playagain_input = playagain_input.upper()
    if playagain_input.upper() == 'Y' or playagain_input.upper() == 'YES':
        return True
    else:
        return False

def main():
    player1 = {'number':1, 'marker':'','position_input':'','position_list':[]}
    player2 = {'number':2, 'marker':'','position_input':'','position_list':[]}
    turn = 0
    board=[' ']* 10
    game_finish = False
    playagain = True
    while not game_finish or playagain:
        if turn == 0:
            while player1['marker'].upper() != 'X' and player1['marker'].upper() != 'O':
                player1['marker'] = input(f'Player 1: Please choose your marker (X or O):')
            player1['marker'] = player1['marker'].upper()
            print(f'Player 1, you are {player1["marker"]}, you play first!')
            displayboard(board)
            player_input(player1, board)
            place_marker(board,player1['marker'], int(player1['position_list'][turn]))
            if player1['marker'] == 'X':
                player2['marker'] = 'O'
            else:
                player2['marker'] = 'X'
        else:
            player_input(player1, board)
            place_marker(board,player1['marker'], int(player1['position_list'][turn]))
            game_finish = game_over(player1,player2)
        if game_finish:
            playagain_input = input('Would you like to play again (Y/N)?')
            if play_again(playagain_input):
                turn = 0
                player1 = {'number':1, 'marker':'','position_input':'','position_list':[]}
                player2 = {'number':2, 'marker':'','position_input':'','position_list':[]}
                board=[' ']* 10
                playagain = True
                game_finish = False
            else:
                break
        else:
            player_input(player2, board)
            place_marker(board,player2['marker'], int(player2['position_list'][turn]))
            game_finish = game_over(player1,player2)
            if game_finish:
                playagain_input = input('Would you like to play again (Y/N)?')
                if play_again(playagain_input):
                    turn = 0
                    player1 = {'number':1, 'marker':'','position_input':'','position_list':[]}
                    player2 = {'number':2, 'marker':'','position_input':'','position_list':[]}
                    board=[' ']* 10
                    playagain = True
                    game_finish = False
                else:
                    break
            else:
                turn += 1
main()
