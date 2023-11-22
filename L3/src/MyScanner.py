import re
from collections import deque
from src import HashTable

class MyScanner:
    def __init__(self, program, token_list):
        self.code_program = program
        self.token_list = token_list
        self.symbol_table = HashTable(1003)
        self.pif = []
        self.current_position = 0
        self.current_line = 1

    def skip_spaces_and_comments(self):
        changed = False
        while self.current_position < len(self.code_program) and self.code_program[self.current_position].isspace():
            if self.code_program[self.current_position] == '\n':
                self.current_line += 1
                changed = True
            self.current_position += 1

        if self.code_program.startswith('//', self.current_position):
            changed = True
            while self.current_position < len(self.code_program) and self.code_program[self.current_position] != '\n':
                self.current_position += 1

        return changed

    def check_strings(self):
        str_regex = re.compile(r'^"([a-zA-Z0-9 ]*)"')
        match = str_regex.match(self.code_program[self.current_position:])
        if match:
            token = match.group(1)
            self.pif.append(("string", -2))
            self.current_position += len(match.group(0))
            return True
        return False

    def check_int(self):
        int_regex = re.compile(r'^([+-]?[1-9]\d*|0)')
        match = int_regex.match(self.code_program[self.current_position:])
        if match:
            token = match.group(1)
            last_value_in_pif = self.pif[-1][1] if self.pif else None
            if (token[0] in ['+', '-'] and last_value_in_pif in [0, -1, -2]) or not last_value_in_pif:
                return False
            self.pif.append(("int", -1))
            self.current_position += len(match.group(0))
            return True
        return False

    def check_token(self):
        for token in self.token_list:
            if self.code_program.startswith(token, self.current_position):
                self.pif.append((token, 0))
                self.current_position += len(token)
                return True
        return False

    def check_constant(self):
        id_regex = re.compile(r'^([a-zA-Z_][a-zA-Z0-9_]*)')
        match = id_regex.match(self.code_program[self.current_position:])
        if match:
            token = match.group(1)
            self.symbol_table.add(token)
            self.pif.append(("identifier", self.symbol_table.get_position(token)))
            self.current_position += len(match.group(0))
            return True
        return False

    def check_characters(self):
        if not self.check_strings() and not self.check_int() and not self.check_token() and not self.check_constant():
            raise Exception(f"Invalid token on line: {self.current_line}")

    def run(self):
        while self.current_position < len(self.code_program):
            while True:
                if not self.skip_spaces_and_comments():
                    break
            if self.current_position == len(self.code_program):
                break
            self.check_characters()
        self.print_to_files()

    def print_to_files(self):
        with open("results/ST.out", "w") as writer:
            writer.write(self.symbol_table.__str__())
        with open("results/PIF.out", "w") as writer:
            for word in self.pif:
                writer.write(f"[{word[0]}:{word[1]}]\n")
