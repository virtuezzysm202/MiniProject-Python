# This is my learn. i want to know how random work. 

import time

class SimpleRandom:
    def __init__(self, seed=None):
        if seed is None:
            seed = int(time.time() * 1000) & 0xFFFFFFFF
        self.state = seed

    def random(self):
        a = 12836289
        c = 2937953728
        m = 2**32
        self.state = (a * self.state + c) % m
        return self.state / m

    def randint(self, low, high):
        return low + int(self.random() * (high - low + 1))

def main():
    rng = SimpleRandom()

    while True:
        print("\n=== Random Number Generator ===")
        print("1. Generate number (1-10)")
        print("2. Exit")

        choice = input("Choose :   (1/2): ")

        if choice == '1':
            num = rng.randint(1, 10)
            print(f"🎲 Random: {num}")
        elif choice == '2':
            print("thx1!")
            break
        else:
            print("Invalid option, try again.")

if __name__ == "__main__":
    main()
1