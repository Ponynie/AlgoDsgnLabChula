from typing import Generator
import pandas as pd

def lab9():
    
    def main():
        path = "lab9/test_case/test.txt"
        kwarg = get_input(path)
        naive = pattern_matching(kwarg, naive_algorithm)
        print_result(naive)
        #kmp = pattern_matching(kwarg, KMP_algorithm)
        #print_result(kmp)

    def pattern_matching(kwarg: dict, matching_algorithm: Generator) -> list[tuple]:
        set_of_alphabet = kwarg["set_of_alphabet"]; num_pattern = kwarg["num_pattern"]; num_text = kwarg["num_text"]; pattern = kwarg["pattern"]; text = kwarg["text"]
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
        pass
    
    def print_result(result: list[tuple]):
        print(len(result), "Answer(s)")
        '''
        for i in result:
            print(i[0], i[1])
        '''
        df = pd.DataFrame(result)
        print(df.to_string(index=False, header=False))
        #df.to_csv("lab9/result.csv", header=["valid shift", "LR/RL"], index=False)

    def get_input(path):
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