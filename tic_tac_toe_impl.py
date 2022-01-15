from tic_tac_toe_blue_print import TicTacToeBluePrint
import random

class TicTacToeImpl(TicTacToeBluePrint):
    def __init__(self):
        self.list_position = {
            1:{"x":0, "y":0},
            2:{"x":0, "y":1},
            3:{"x":0, "y":2},
            4:{"x":1, "y":0},
            5:{"x":1, "y":1},
            6:{"x":1, "y":2},
            7:{"x":2, "y":0},
            8:{"x":2, "y":1},
            9:{"x":2, "y":2},
        }
        self.map = [["1","2","3"],["4","5","6"],["7","8","9"]]
        self.is_continue = True

    def fill_the_player_input(self, player_type, position):
        selected_position = self.list_position[position]
        try:
            int(self.map[selected_position['x']][selected_position['y']])
            if player_type == 1:
                x = selected_position['x']
                y = selected_position['y']
                self.map[x][y] = 'X'
            else:
                x = selected_position['x']
                y = selected_position['y']
                self.map[x][y] = 'O'
            self.validate_winning()
        except Exception:
            print("Position already filled")

    
    def validate_winning(self):
        list_stil_play = []
        for x in range(0,3):
            for y in range(0,3):
                try:
                    parse_val = int(self.map[x][y])
                    list_stil_play.append(parse_val)
                except Exception:
                    pass
        
        if len(list_stil_play)==0:
            self.print_map()
            print("Draw") 
            self.is_continue = False
        elif self.map[0][0] == "X" and self.map[0][1] =="X" and self.map[0][2]=="X":
            self.print_map()
            print(f"{self.first_player_name} Win")
            self.is_continue = False
        elif self.map[1][0] == "X" and self.map[1][1] =="X" and self.map[1][2]=="X":
            self.print_map()
            print(f"{self.first_player_name} Win")
            self.is_continue = False
        elif self.map[2][0] == "X" and self.map[2][1] =="X" and self.map[2][2]=="X":
            self.print_map()
            print(f"{self.first_player_name} Win")
            self.is_continue = False
        elif self.map[0][0] == "X" and self.map[1][0] =="X" and self.map[2][0]=="X":
            self.print_map()
            print(f"{self.first_player_name} Win")
            self.is_continue = False
        elif self.map[0][1] == "X" and self.map[1][1] =="X" and self.map[2][1]=="X":
            self.print_map()
            print(f"{self.first_player_name} Win")
            self.is_continue = False
        elif self.map[0][2] == "X" and self.map[1][2] =="X" and self.map[2][2]=="X":
            self.print_map()
            print(f"{self.first_player_name} Win")
            self.is_continue = False
        elif self.map[0][0] == "X" and self.map[1][1] =="X" and self.map[2][2]=="X":
            self.print_map()
            print(f"{self.first_player_name} Win")
            self.is_continue = False
        elif self.map[2][0] == "X" and self.map[1][1] =="X" and self.map[0][2]=="X":
            self.print_map()
            print(f"{self.first_player_name} Win")
            self.is_continue = False

        # Check For player 2
        if self.map[0][0] == "O" and self.map[0][1] =="O" and self.map[0][2]=="O":
            self.print_map()
            print(f"{self.second_player_name} Win")
            self.is_continue = False
        elif self.map[1][0] == "O" and self.map[1][1] =="O" and self.map[1][2]=="O":
            self.print_map()
            print(f"{self.second_player_name} Win")
            self.is_continue = False
        elif self.map[2][0] == "O" and self.map[2][1] =="O" and self.map[2][2]=="O":
            self.print_map()
            print(f"{self.second_player_name} Win")
            self.is_continue = False
        elif self.map[0][0] == "O" and self.map[1][0] =="O" and self.map[2][0]=="O":
            self.print_map()
            print(f"{self.second_player_name} Win")
            self.is_continue = False
        elif self.map[0][1] == "O" and self.map[1][1] =="O" and self.map[2][1]=="O":
            self.print_map()
            print(f"{self.second_player_name} Win")
            self.is_continue = False
        elif self.map[0][2] == "O" and self.map[1][2] =="O" and self.map[2][2]=="O":
            self.print_map()
            print(f"{self.second_player_name} Win")
            self.is_continue = False
        elif self.map[0][0] == "O" and self.map[1][1] =="O" and self.map[2][2]=="O":
            self.print_map()
            print(f"{self.second_player_name} Win")
            self.is_continue = False
        elif self.map[2][0] == "O" and self.map[1][1] =="O" and self.map[0][2]=="O":
            self.print_map()
            print("Player 2 Win")
            self.is_continue = False
    
    
    def computer_movement(self):
        list_computer_movement = []
        for step_x in range(0, 3):
            for step_y in range(0,3):
                if (self.map[step_x][step_y]!='X') and (self.map[step_x][step_y]!='O'):
                    val_selected = self.map[step_x][step_y]
                    list_computer_movement.append(val_selected)
        random_movement = random.randint(0, len(list_computer_movement)-1)
        print("Computer Movement ")
        self.fill_the_player_input(2, int(list_computer_movement[random_movement]))
    
    
    def print_map(self):
        for cordinate_x in self.map:
            print(cordinate_x)

    def set_player_name(self, first_player_name, second_player_name):
        self.first_player_name = first_player_name
        self.second_player_name = second_player_name

    def get_is_continue(self):
        return self.is_continue