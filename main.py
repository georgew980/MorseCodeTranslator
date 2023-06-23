import winsound
import time


class MorseCodeConverter:
    def __init__(self):
        self.morse_code = {
            'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
            'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
            'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
            'Y': '-.--', 'Z': '--..', '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
            '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.', '.': '.-.-.-', ',': '--..--',
            '?': '..--..', "'": '.----.', '!': '-.-.--', '/': '-..-.', '(': '-.--.', ')': '-.--.-', '&': '.-...',
            ':': '---...', ';': '-.-.-.', '=': '-...-', '+': '.-.-.', '-': '-....-', '_': '..--.-', '"': '.-..-.',
            '$': '...-..-', '@': '.--.-.', ' ': '/'
        }
        # The Morse code dictionary maps each character to its corresponding Morse code representation.
        # Keys are characters, and values are Morse code symbols or sequences.
        self.dot_duration = 100  # milliseconds

    def convert_to_morse_code(self, message):
        morse_message = ''  # Initialize an empty string to store the Morse code message
        for char in message:
            if char.upper() in self.morse_code:  # Check if the character is in the Morse code dictionary
                morse_code = self.morse_code[char.upper()]  # Get the Morse code representation of the character
                morse_message += morse_code + ' '  # Append the Morse code to the message string with a space separator

                # Iterate over each symbol (dot or dash) in the Morse code representation
                for symbol in morse_code:
                    if symbol == '.':  # If it is a dot, play a dot sound
                        self.play_dot()
                    elif symbol == '-':  # If it is a dash, play a dash sound
                        self.play_dash()
                    else:  # If it is a space, pause for a duration equal to two dots
                        time.sleep(self.dot_duration * 2 / 1000)

                # Pause for a duration equal to one dot between characters
                time.sleep(self.dot_duration / 1000)
            else:
                # If the character is not in the Morse code dictionary, simply append it to the message as is
                morse_message += char

        return morse_message

    def play_dot(self):
        winsound.Beep(1000, self.dot_duration)  # Play a beep sound for a dot

    def play_dash(self):
        winsound.Beep(1000, self.dot_duration * 3)  # Play a beep sound for a dash


converter = MorseCodeConverter()  # Create an instance of the MorseCodeConverter class

try:
    while True:  # Enter an infinite loop to continuously receive user input
        user_input = input("Enter a message (or 'exit' to quit): ")  # Prompt the user to enter a message
        if user_input.lower() == 'exit':  # If the user enters 'exit', break the loop and exit the program
            break
        morse_output = converter.convert_to_morse_code(user_input)  # Convert the user's input to Morse code
        print("Morse code:", morse_output)  # Print the Morse code representation of the user's input
except KeyboardInterrupt:
    print("\nProgram terminated by user.")  # If the user interrupts the program, print a termination message

