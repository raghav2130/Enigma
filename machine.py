from random import shuffle
import string

def shuffle_word(word):
    word = list(word)
    shuffle(word)
    return ''.join(word)

class Enigma:
    def __init__(self):
        # each rotor have all 26 letter
        # there are 5 rotors to choose from and each has diffrent taglement inside
        # you can make your own scramble if you want
        self.rotor1 = "VSUBWXNKMFPYLTJODZEAGICRQH" 
        self.rotor2 = "DYTIQAUHPGLNXZCSBJVKEFWOMR" 
        self.rotor3 = "IREMVTAZXDOHGUPWBJCYSLQNKF" 
        self.rotor4 = "FUBYAMPDGTJVILOEWZSRNHQCXK" 
        self.rotor5 = "ZYURNOJBIKWMQDPVGXCHEFLAST"

        # choose 3 of them without  repeating
        self.rotors = [ self.rotor1, self.rotor2, self.rotor3 ]
        self.plugboard = {} # plugboard to map a letter to another one
        self.rotor_position = [0, 0, 0]  # set initial rotor positions

    def set_rotor_position(self, pos):
        self.rotor_position = pos

    def set_plugboard(self, plugboard_mapping):
        self.plugboard = plugboard_mapping

    def rotate_rotors(self):
        self.rotor_position[0] = (self.rotor_position[0] + 1) % 26
        if self.rotor_position[0] == 0:
            self.rotor_position[1] = (self.rotor_position[1] + 1) % 26
            if self.rotor_position[1] == 0:
                self.rotor_position[2] = (self.rotor_position[2] + 1) % 26

    def encrypt(self, text):
        text = text.upper()
        result = []
        for char in text:
            if char == " ":
                result.append(char)

            #pass through plugboard
            char = self.plugboard.get(char, char) 

            #pass through 3 rotors 
            for i in range(3):
                idx = (self.rotors[i].index(char) + self.rotor_position[i]) % 26
                char = self.rotors[i][idx]

            #pass through plugboard again
            char = self.plugboard.get(char, char)

            result.append(char)
            #rotating rots after each letter/char
            self.rotate_rotors()

        return ''.join(result)

