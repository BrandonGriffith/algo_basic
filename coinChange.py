class CoinChange:
    def brute_force(self, coins, amount):
        if amount == 0:
            return 0
        if amount < 0:
            return -1
        res = (amount + 1)
        for coin in coins:
            sub_res = self.brute_force(coins, amount - coin)
            if sub_res >= 0:
                res = min(res, 1 + sub_res)
        return res if res != (amount + 1) else -1

    def memoization(self, coins, amount):
        memo = {0 : 0}
        def dp(a):
            if a in memo:
                return memo[a]
            if a < 0:
                return a
            res = (a + 1)
            for coin in coins:
                sub_res = dp(a - coin)
                if sub_res >= 0:
                    res = min(res, 1 + sub_res)
            memo[a] = res if res != (a + 1) else -1
            return memo[a]
        return dp(amount)

def get_input():
    coins = input("Enter coin denominations (space-separated): ")
    coins = [int(c) for c in coins.strip().split()]
    while True:
        amount_input = input("Enter amount to make change for: ")
        if amount_input.isdigit():
            amount = int(amount_input)
            break
        print("Invalid input. Please enter a valid integer.")
    return coins, amount

def main():
    coin_change = CoinChange()
    while True:
        method = input("Choose method ('brute', 'memo' or 'exit'): ").strip().lower()
        if method == 'exit':
            break
        if method not in ['brute', 'memo']:
            print("Invalid choice. Please choose 'brute', 'memo' or 'exit'.")
            continue
        coins, amount = get_input()
        if method == 'brute':
            result = coin_change.brute_force(coins, amount)
        else:
            result = coin_change.memoization(coins, amount)
        if result == -1:
            print(f"Cannot make change for {amount} with given coins.")
        else:
            print(f"Minimum coins needed: {result}")

if __name__ == "__main__":
    main()