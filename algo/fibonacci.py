class Fibonacci:
    def brute_force(x : int) -> int:
        if x <= 1:
            return x
        return Fibonacci.brute_force(x - 1) + Fibonacci.brute_force(x - 2)

    def memoization(x : int) -> int:
        if x <= 1:
            return x
        memo = [0] * (x + 1)
        memo[1] = 1
        for i in range(2, x + 1):
            memo[i] = memo[i - 1] + memo[i - 2]
        return memo[x]

    def tabulation(x : int) -> int:
        if x <= 1:
            return x
        a, b = 0, 1
        for _ in range(x-1):
            a, b = b, a + b
        return b

def get_number():
    while True:
        number = input("Enter a number: ")
        if number.isdigit():
            return int(number)
        print("Invalid input. Please enter a valid integer.")

def main():
    while True:
        method = input("Choose method ('brute', 'memo', 'tab' or 'exit'): ").strip().lower()
        if method == 'brute':
            print(Fibonacci.brute_force(get_number()))
        elif method == 'memo':
            print(Fibonacci.memoization(get_number()))
        elif method == 'tab':
            print(Fibonacci.tabulation(get_number()))
        elif method == 'exit':
            break
        else:
            print("Invalid choice. Please choose 'brute', 'memo' or 'exit'.")

if __name__ == "__main__":
    main()