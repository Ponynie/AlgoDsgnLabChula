def lab8():
    
    
    def main():
        path = "lab8/test_case/test.txt"
        n = read_input(path)
        origin_sequnce = [i for i in range(0, n+1)]
        new_sequence = [-1 for _ in range(0, n+1)]
        create_sequence(origin_sequnce, new_sequence)
        print("-"*20)
        print(f"Origin sequence: {origin_sequnce}")
        print(f"New sequence: {new_sequence}")
        print("-"*20)
        
        
    def read_input(arg = None) -> int:
        if arg is None:
            return int(input("Enter a number: "))
        elif isinstance(arg, str):
            with open(arg, 'r') as f:
                return int(f.readline().strip())
        else:
            raise TypeError('Invalid type for read_input')


    def create_sequence(sequence: list, buffer: list) -> None:
        pass

    main()
    
lab8()