import threading
import time
import random

THINKING = 0
HUNGRY = 1
EATING = 2

NUM_PHILOSOPHERS = 5

class DiningPhilosophers:
    def __init__(self):
        # what are the philosophers up to
        self.state = [THINKING] * NUM_PHILOSOPHERS
        # lock for thread safety
        self.lock = threading.Lock()
        # condition variable for each philosopher
        self.conditions = [threading.Condition(self.lock) for i in range(NUM_PHILOSOPHERS)]
        # left neighbor check
    def left(self, i):
        return(i - 1) % NUM_PHILOSOPHERS
# right neighbor check
    def right(self, i):
        return (i + 1) % NUM_PHILOSOPHERS
# can the philosophers eat
    def test(self, i):
        if (self.state[i] == HUNGRY and self.state[self.left(i)] != EATING and self.state[self.right(i)] != EATING):

            self.state[i] = EATING
            print(f"Philospher {i} is EATING")
            self.conditions[i].notify()
# Philosophers pick up the forks
    def pickup_forks(self, i):
        with self.lock:
            self.state[i] = HUNGRY
            print(f"Philosopher {i} is HUNGRY")

            self.test(i)

            while self.state[i] != EATING:
                self.conditions[i].wait()
# philosophers put the forks down
    def return_forks(self, i):
        with self.lock:
            self.state[i] = THINKING
            print(f"Philospher {i} finished eating")

            self.test(self.left(i))
            self.test(self.right(i))


class Philosopher(threading.Thread):
    def __init__(self, id, table):
        threading.Thread.__init__(self)
        self.id = id
        self.table = table

    def run(self):
        for i in range(5):
            print(f"Philospher {self.id} is thinking...")
            time.sleep(random.randint(1,3))

            self.table.pickup_forks(self.id)

            time.sleep(random.randint(1, 3))

            self.table.return_forks(self.id)

        print(f"Philospher {self.id} is done!")
def main():
    print("Starting Dining Philosphers problem")
    print("-" * 40)

    table = DiningPhilosophers()

    philosophers = []
    for i in range(NUM_PHILOSOPHERS):
        p = Philosopher(i, table)
        philosophers.append(p)

    for p in philosophers:
        p.start()

    for p in philosophers:
        p.join()

    print("-" * 40)
    print("Everyone finished eating")

if __name__ == "__main__":
    main()




