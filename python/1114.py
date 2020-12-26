"""
1114. Print in Order
Easy

Suppose we have a class:

public class Foo {
  public void first() { print("first"); }
  public void second() { print("second"); }
  public void third() { print("third"); }
}
The same instance of Foo will be passed to three different threads. Thread A will call first(), thread B will call second(), and thread C will call third(). Design a mechanism and modify the program to ensure that second() is executed after first(), and third() is executed after second().

Example 1:

Input: [1,2,3]
Output: "firstsecondthird"
Explanation: There are three threads being fired asynchronously. The input [1,2,3] means thread A calls first(), thread B calls second(), and thread C calls third(). "firstsecondthird" is the correct output.
Example 2:

Input: [1,3,2]
Output: "firstsecondthird"
Explanation: The input [1,3,2] means thread A calls first(), thread B calls third(), and thread C calls second(). "firstsecondthird" is the correct output.
 
Note:
We do not know how the threads will be scheduled in the operating system, even though the numbers in the input seems to imply the ordering. The input format you see is mainly to ensure our tests' comprehensiveness.
"""

class Foo:
    def __init__(self):
        self._first = False
        self._second = False


    def first(self, printFirst: 'Callable[[], None]') -> None:
        
        # printFirst() outputs "first". Do not change or remove this line.
        printFirst()
        self._first = True


    def second(self, printSecond: 'Callable[[], None]') -> None:
        while not self._first:
            pass
        
        # printSecond() outputs "second". Do not change or remove this line.
        printSecond()
        self._second = True


    def third(self, printThird: 'Callable[[], None]') -> None:
        while not self._second:
            pass
        # printThird() outputs "third". Do not change or remove this line.
        printThird()

from threading import Semaphore
class Foo1:
    def __init__(self):
        self.gates = (Semaphore(0),Semaphore(0))


    def first(self, printFirst: 'Callable[[], None]') -> None:
        
        # printFirst() outputs "first". Do not change or remove this line.
        printFirst()
        self.gates[0].release()


    def second(self, printSecond: 'Callable[[], None]') -> None:
        
        # printSecond() outputs "second". Do not change or remove this line.
        with self.gates[0]:
            printSecond()
            self.gates[1].release()


    def third(self, printThird: 'Callable[[], None]') -> None:
        
        # printThird() outputs "third". Do not change or remove this line.
        with self.gates[1]:
            printThird()
            self.gates[1].release()