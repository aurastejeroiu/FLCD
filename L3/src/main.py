
from src import MyScanner
from result import *
from src.FiniteAutomation import FiniteAutomation


class Main:
    def __init__(self):
        self.fa = FiniteAutomation("result/FA.in")

    def main(self):
        done = False
        while not done:
            self.print_menu()
            option = int(input("command: "))
            if option == 1:
                print(self.fa.compute_data())
            elif option == 2:
                if self.fa.check_if_deterministic():
                    sequence = input("Your sequence: ")
                    if self.fa.check_sequence(sequence):
                        print("Sequence is valid")
                    else:
                        print("Invalid sequence")
                else:
                    print("FA is not deterministic.")
            elif option == 3:
                self.run_scanner()
            else:
                done = True

    @staticmethod
    def print_menu():
        print("1. Print data.")
        print("2. Check if sequence is accepted by DFA.")
        print("3. Run scanner.")
        print("0. Exit")

    def run_scanner(self):
        try:
            with open("results/Example.in", "r") as file_content:
                string_content = file_content.read()
            with open("results/Token.in", "r") as tokens_file:
                token_list = [line.strip() for line in tokens_file.readlines()]
            scanner = MyScanner(string_content, token_list)
            try:
                scanner.run()
            except Exception as e:
                print(e)
        except IOError:
            print("Can't read input files.")

if __name__ == "__main__":
    main_instance = Main()
    main_instance.main()
