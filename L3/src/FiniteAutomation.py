import os
from Scanner import *

class FiniteAutomation:
    def __init__(self, file_name):
        self.all_state_list = set()
        self.alphabet = set()
        self.final_states = set()
        self.transitions = {}
        self.split_file(file_name)

    def split_file(self, file_name):
        try:
            with open(file_name, 'r') as file:
                states_list = file.readline().strip().split()
                self.all_state_list = set(states_list)
                alphabet_list = file.readline().strip().split()
                self.alphabet = set(alphabet_list)
                self.initial_state = file.readline().strip()
                final_states_line = file.readline().strip()
                self.final_states = set(final_states_line.split())

                for line in file:
                    transition_list = line.strip().split()
                    if (transition_list[0] in self.all_state_list and
                            transition_list[2] in self.all_state_list and
                            transition_list[1] in self.alphabet):
                        transition_states = (transition_list[0], transition_list[1])
                        if transition_states in self.transitions:
                            self.transitions[transition_states].add(transition_list[2])
                        else:
                            self.transitions[transition_states] = {transition_list[2]}

        except FileNotFoundError:
            print("File not found.")
        except Exception as e:
            print(f"An error occurred: {e}")

    def compute_data(self):
        result = []
        result.append("Alphabet: " + " ".join(self.alphabet))
        result.append("All State List: " + " ".join(self.all_state_list))
        result.append("Final states: " + " ".join(self.final_states))
        result.append("Transitions:")
        for key, value in self.transitions.items():
            result.append(f"<{key[0]}, {key[1]}> -> {value}")
        return "\n".join(result)

    def check_if_deterministic(self):
        for transition in self.transitions.values():
            if len(transition) > 1:
                return False
        return True

    def check_sequence(self, sequence):
        if not sequence:
            return False
        state = self.initial_state
        for char in sequence:
            transition_key = (state, char)
            if transition_key in self.transitions:
                state = next(iter(self.transitions[transition_key]))
            else:
                return False
        return True
