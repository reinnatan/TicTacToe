from abc import ABC, abstractclassmethod, abstractmethod

class TicTacToeBluePrint(ABC):
    @abstractmethod
    def fill_the_player_input(self,player_type, position):
        pass

    @abstractmethod
    def validate_winning(self):
        pass
    
    @abstractmethod
    def computer_movement(self):
        pass
    
    @abstractmethod
    def print_map(self):
        pass

    @abstractmethod
    def set_player_name(self, first_player_name, second_player_name):
        pass

    @abstractmethod
    def get_is_continue(self):
        pass