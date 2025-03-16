import process from "node:process";
import { createInterface } from "node:readline";
class CoinChange {
    bruteForce(coins, amount) {
        if (amount === 0) {
            return 0;
        }
        if (amount < 0) {
            return -1;
        }
        let res = amount + 1;
        for (const coin of coins) {
            const subRes = this.bruteForce(coins, amount - coin);
            if (subRes >= 0) {
                res = Math.min(res, 1 + subRes);
            }
        }
        return res !== (amount + 1) ? res : -1;
    }
    memoization(coins, amount) {
        const memo = { 0: 0 };
        const dp = (a) => {
            if (a in memo) {
                return memo[a];
            }
            if (a < 0) {
                return a;
            }
            let res = a + 1;
            for (const coin of coins) {
                const subRes = dp(a - coin);
                if (subRes >= 0) {
                    res = Math.min(res, 1 + subRes);
                }
            }
            memo[a] = res !== (a + 1) ? res : -1;
            return memo[a];
        };
        return dp(amount);
    }
}
const rl = createInterface({
    input: process.stdin,
    output: process.stdout,
});
function question(prompt) {
    return new Promise((resolve) => {
        rl.question(prompt, (answer) => {
            resolve(answer);
        });
    });
}
async function getInput() {
    const coinsInput = await question("Enter coin denominations (space-separated): ");
    const coins = coinsInput.split(" ").map((c) => parseInt(c, 10));
    let amount = 0;
    while (true) {
        const amountInput = await question("Enter amount to make change for: ");
        if (/^\d+$/.test(amountInput)) {
            amount = parseInt(amountInput, 10);
            break;
        }
        else {
            console.log("Invalid input. Please enter a valid integer.");
        }
    }
    return [coins, amount];
}
async function main() {
    const coinChange = new CoinChange();
    const processMethod = async () => {
        const method = await question("Choose method ('brute', 'memo' or 'exit'): ");
        const methodLower = method.trim().toLowerCase();
        if (methodLower === "exit") {
            rl.close();
            return;
        }
        if (methodLower !== "brute" && methodLower !== "memo") {
            console.log("Invalid choice. Please choose 'brute', 'memo' or 'exit'.");
            return processMethod();
        }
        try {
            const [coins, amount] = await getInput();
            let result;
            if (methodLower === "brute") {
                result = coinChange.bruteForce(coins, amount);
            }
            else {
                result = coinChange.memoization(coins, amount);
            }
            if (result === -1) {
                console.log(`Cannot make change for ${amount} with given coins.`);
            }
            else {
                console.log(`Minimum coins needed: ${result}`);
            }
        }
        catch (error) {
            console.error("An error occurred:", error);
        }
        return processMethod();
    };
    await processMethod();
}
main();
