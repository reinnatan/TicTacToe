import random

from tic_tac_toe_impl import TicTacToeImpl

if '__main__' == __name__:
    print("Tic Tac Toe")
    tic_tac_toe_impl = TicTacToeImpl()
    list_number = [1,2,3,4,5,6,7,8,9]
    current_player = 1

    play_computer = input("Play With computer (Y/N): ")
    if play_computer.lower() == "n":
        first_player_name = input("Player 1 Name : ")
        second_player_name = input("Player 2 Name : ")
        tic_tac_toe_impl.set_player_name(first_player_name, second_player_name)
        is_continue = tic_tac_toe_impl.get_is_continue()

        while is_continue:
            tic_tac_toe_impl.print_map()
            if current_player == 1:
                player_1 = input(f"{first_player_name} : ")
                try:
                    player_1_input_parse = int(player_1)
                    if player_1_input_parse not in list_number:
                        print("Please input valid number from 1-9")
                    else:
                        tic_tac_toe_impl.fill_the_player_input(current_player, player_1_input_parse)
                        is_continue = tic_tac_toe_impl.get_is_continue()
                    current_player = 2
                except Exception:
                    print("Please input number")
            else:
                player_2 = input(f"{second_player_name} : ")
                try:
                    player_2_input_parse = int(player_2)
                    if player_2_input_parse not in list_number:
                        print("Please input valid number from 1-9")
                    else:
                        tic_tac_toe_impl.fill_the_player_input(current_player, player_2_input_parse)
                        is_continue = tic_tac_toe_impl.get_is_continue()
                    current_player = 1
                except Exception:
                    print("Please input number")
    elif play_computer.lower() == "y":
        first_player_name = input("Player Name : ")
        tic_tac_toe_impl.set_player_name(first_player_name, "Computer")
        is_continue = tic_tac_toe_impl.get_is_continue()
        while is_continue:
            tic_tac_toe_impl.print_map()
            if current_player == 1:
                player_1 = input(f"{first_player_name} : ")
                try:
                    player_1_input_parse = int(player_1)
                    if player_1_input_parse not in list_number:
                        print("Please input valid number from 1-9")
                    else:
                        tic_tac_toe_impl.fill_the_player_input(current_player, player_1_input_parse)
                        is_continue = tic_tac_toe_impl.get_is_continue()
                    current_player = 2
                except Exception:
                    print("Please input number")
            else:
                tic_tac_toe_impl.computer_movement()
                is_continue = tic_tac_toe_impl.get_is_continue()
                current_player = 1
                
    else:
        print("invalid choise input")
    
