import process from "node:process";
import { createInterface } from "node:readline";

class CoinChange {
  bruteForce(coins: number[], amount: number): number {
    if (amount === 0) {
      return 0;
    }
    if (amount < 0) {
      return -1;
    }
    let res: number = amount + 1;
    for (const coin of coins) {
      const subRes: number = this.bruteForce(coins, amount - coin);
      if (subRes >= 0) {
        res = Math.min(res, 1 + subRes);
      }
    }
    return res !== (amount + 1) ? res : -1;
  }

  memoization(coins: number[], amount: number): number {
    const memo: Record<number, number> = { 0: 0 };

    const dp = (a: number): number => {
      if (a in memo) {
        return memo[a];
      }
      if (a < 0) {
        return a;
      }
      let res: number = a + 1;
      for (const coin of coins) {
        const subRes: number = dp(a - coin);
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

function question(prompt: string): Promise<string> {
  return new Promise((resolve) => {
    rl.question(prompt, (answer: string) => {
      resolve(answer);
    });
  });
}

async function getInput(): Promise<[number[], number]> {
  const coinsInput: string = await question(
    "Enter coin denominations (space-separated): ",
  );
  const coins: number[] = coinsInput.split(" ").map((c) => parseInt(c, 10));

  let amount: number = 0;
  while (true) {
    const amountInput: string = await question(
      "Enter amount to make change for: ",
    );
    if (/^\d+$/.test(amountInput)) {
      amount = parseInt(amountInput, 10);
      break;
    } else {
      console.log("Invalid input. Please enter a valid integer.");
    }
  }

  return [coins, amount];
}

async function main(): Promise<void> {
  const coinChange: CoinChange = new CoinChange();

  const processMethod = async (): Promise<void> => {
    const method: string = await question(
      "Choose method ('brute', 'memo' or 'exit'): ",
    );
    const methodLower: string = method.trim().toLowerCase();

    if (methodLower === "exit") {
      rl.close();
      return;
    }

    if (methodLower !== "brute" && methodLower !== "memo") {
      console.log("Invalid choice. Please choose 'brute', 'memo' or 'exit'.");
      return processMethod();
    }

    try {
      const [coins, amount]: [number[], number] = await getInput();

      let result: number;
      if (methodLower === "brute") {
        result = coinChange.bruteForce(coins, amount);
      } else {
        result = coinChange.memoization(coins, amount);
      }

      if (result === -1) {
        console.log(`Cannot make change for ${amount} with given coins.`);
      } else {
        console.log(`Minimum coins needed: ${result}`);
      }
    } catch (error: unknown) {
      console.error("An error occurred:", error);
    }

    return processMethod();
  };

  await processMethod();
}

main();
