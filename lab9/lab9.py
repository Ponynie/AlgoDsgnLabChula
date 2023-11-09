from typing import Generator
import pandas as pd

def lab9():
    
    def main():
        path = "lab9/test_case/test.txt"
        kwargs = get_input(path)
        print_result(pattern_matching(kwargs, naive_algorithm), to_csv=False)
        print("π:", *calculate_pi(kwargs["pattern"]))
        print_result(pattern_matching(kwargs, KMP_algorithm), to_csv=False)

    def pattern_matching(kwargs: dict, matching_algorithm: Generator) -> list[tuple]:
        set_of_alphabet = kwargs["set_of_alphabet"]; num_pattern = kwargs["num_pattern"]; num_text = kwargs["num_text"]; pattern = kwargs["pattern"]; text = kwargs["text"]
        result_LR = []
        result_RL = []
        
        for i in matching_algorithm(set_of_alphabet, num_pattern, num_text, pattern, text):
            result_LR.append((i+1, "LR"))
        result_LR.sort(key = lambda x: x[0])
        
        for i in matching_algorithm(set_of_alphabet, num_pattern, num_text, pattern, text[::-1]):
            result_RL.append((num_text - i, "RL"))
        result_RL.sort(key = lambda x: x[0])
        
        return result_LR + result_RL
    
    def naive_algorithm(set_of_alphabet: set, num_pattern: int, num_text: int, pattern: str, text: str) -> int:
        for s in range(num_text - num_pattern + 1):
            if pattern == text[s:s+num_pattern]:
                yield s    

    def KMP_algorithm(set_of_alphabet: set, num_pattern: int, num_text: int, pattern: str, text: str) -> int:
        pi = calculate_pi(pattern)
        j = 0
        for i in range(num_text):
            while j > 0 and text[i] != pattern[j]:
                j = pi[j-1]
            if text[i] == pattern[j]:
                if j == num_pattern - 1:
                    yield i - num_pattern + 1
                    j = pi[j]
                else:
                    j += 1
    
    def calculate_pi(pattern: str) -> list[int]:
        pi = [0] * len(pattern)
        j = 0
        for i in range(1, len(pattern)):
            while j > 0 and pattern[i] != pattern[j]:
                j = pi[j-1]
            if pattern[i] == pattern[j]:
                j += 1
                pi[i] = j
        return pi
    
    def print_result(result: list[tuple], to_csv: bool = False) -> None:
        print("-"*30)
        print(len(result), "Answer(s)")
        '''
        for i in result:
            print(i[0], i[1])
        '''
        df = pd.DataFrame(result)
        print(df.to_string(index=False, header=False))
        print("-"*30)
        if to_csv: 
            df.to_csv("lab9/result.csv", header=["valid shift", "LR/RL"], index=False)

    def get_input(path: str) -> dict:
        with open(path, 'r') as f:
            lines = [next(f).strip() for _ in range(4)]
            lines = [tuple(i.split(" ")) for i in lines]
            kwarg = dict()
            kwarg["set_of_alphabet"] = set(lines[0])
            kwarg["num_pattern"] = int(lines[1][0])
            kwarg["num_text"] = int(lines[1][1])
            kwarg["pattern"] = ''.join(lines[2])
            kwarg["text"] = ''.join(lines[3])
        return kwarg
    
    
    main()
    
lab9()