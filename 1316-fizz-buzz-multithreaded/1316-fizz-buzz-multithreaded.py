from threading import Condition

class FizzBuzz:
    def __init__(self, n: int):
        self.n = n
        self.i = 1
        self.condition = Condition()


    def fizz(self, printFizz: 'Callable[[], None]') -> None:
        while True:
            with self.condition:
                while self.i <= self.n and (self.i % 3 != 0 or self.i % 5 == 0):
                    # 不满足条件，释放锁并等待
                    # 线程主动让出执行权，等待条件变化
                    self.condition.wait()
                if self.i > self.n: return
                printFizz()
                self.i += 1
                # 通知所有等待的线程，“条件可能已变化，请重新检查”
                self.condition.notify_all()


    # printBuzz() outputs "buzz"
    def buzz(self, printBuzz: 'Callable[[], None]') -> None:
        while True:
            with self.condition:
                while self.i <= self.n and (self.i % 5 != 0 or self.i % 3 == 0):
                    self.condition.wait()
                if self.i > self.n: return 
                printBuzz()
                self.i += 1
                self.condition.notify_all()
    	

    # printFizzBuzz() outputs "fizzbuzz"
    def fizzbuzz(self, printFizzBuzz: 'Callable[[], None]') -> None:
        while True:
            with self.condition:
                while self.i <= self.n and (self.i % 5 != 0 or self.i % 3 != 0):
                    self.condition.wait()
                if self.i > self.n: return 
                printFizzBuzz()
                self.i += 1
                self.condition.notify_all()
        

    # printNumber(x) outputs "x", where x is an integer.
    def number(self, printNumber: 'Callable[[int], None]') -> None:
        while True:
            with self.condition:
                while self.i <= self.n and (self.i % 5 == 0 or self.i % 3 == 0):
                    self.condition.wait()
                if self.i > self.n: return 
                printNumber(self.i)
                self.i += 1
                self.condition.notify_all()
        