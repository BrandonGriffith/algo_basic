class CoinChange {
  bruteForce(coins: number[], amount: number): number {
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

  memoization(coins: number[], amount: number): number {
    const memo: Record<number, number> = { 0: 0 };

    const dp = (a: number): number => {
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

async function readLine(prompt: string): Promise<string> {
  const buf = new Uint8Array(1024);
  await Deno.stdout.write(new TextEncoder().encode(prompt));
  const n = await Deno.stdin.read(buf);
  if (n === null) return "";
  return new TextDecoder().decode(buf.subarray(0, n)).trim();
}

async function getInput(): Promise<[number[], number]> {
  const coinsInput = await readLine(
    "Enter coin denominations (space-separated): ",
  );
  const coins = coinsInput.split(" ").map((c) => parseInt(c, 10));

  let amount = 0;
  while (true) {
    const amountInput = await readLine("Enter amount to make change for: ");
    if (/^\d+$/.test(amountInput)) {
      amount = parseInt(amountInput, 10);
      break;
    } else {
      console.log("Invalid input. Please enter a valid integer.");
    }
  }

  return [coins, amount];
}

async function main() {
  const coinChange = new CoinChange();

  const processMethod = async (): Promise<void> => {
    const method = await readLine(
      "Choose method ('brute', 'memo' or 'exit'): ",
    );
    const methodLower = method.trim().toLowerCase();

    if (methodLower === "exit") {
      return;
    }

    if (methodLower !== "brute" && methodLower !== "memo") {
      console.log("Invalid choice. Please choose 'brute', 'memo' or 'exit'.");
      return processMethod();
    }

    try {
      const [coins, amount] = await getInput();

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
    } catch (error) {
      console.error("An error occurred:", error);
    }

    return processMethod();
  };

  await processMethod();
}

if (import.meta.main) {
  main().catch(console.error);
}

export { CoinChange };
