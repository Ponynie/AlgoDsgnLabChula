def lab8():
    
    
    def main():
        path = "lab8/test_case/test.txt"
        n = read_input(path)
        sequence = [i for i in range(0, n+1)]
        bufferDC = []
        bufferNDC = []
        
        sort_sequence_DC(sequence, bufferDC)
        sort_sequence_NDC(sequence, bufferNDC)
        
        print("-"*40)
        print("n:", n)
        print("sequence D&C:", *bufferDC, check_correctness(sequence, bufferDC))
        #print("sequence Non-D&C:", *bufferNDC, check_correctness(sequence, bufferNDC))
        print("-"*40)
        
        
    def read_input(arg = None) -> int:
        if arg is None:
            return int(input("Enter a number: "))
        elif isinstance(arg, str):
            with open(arg, 'r') as f:
                return int(f.readline().strip())
        else:
            raise TypeError('Invalid type for read_input')

    def sort_sequence_DC(sequence: list, buffer: list) -> None:
        if len(sequence) > 1:
            # divide
            even = [elem for idx, elem in enumerate(sequence) if idx % 2 == 0]
            odd = [elem for idx, elem in enumerate(sequence) if idx % 2 != 0]
            sort_sequence_DC(even, buffer)
            sort_sequence_DC(odd, buffer)
        else:
            buffer.append(sequence[0])

    def generate_condition(sequence: list) -> tuple:
        for i in range(1, len(sequence)):
            border = min((len(sequence)-1)-i, i-0)
            for j in range(1, border+1):
                yield (sequence[i-j], sequence[i], sequence[i+j])
    
    def check_correctness(sequence: list, buffer: list) -> bool:
        for condition in generate_condition(sequence):
            x1_idx = buffer.index(condition[0])
            x2_idx = buffer.index(condition[1])
            x3_idx = buffer.index(condition[2])
            if x1_idx < x2_idx < x3_idx:
                return False
        return True

    def sort_sequence_NDC(sequence: list, buffer) -> None:
        pass
    
    main()
    
lab8()