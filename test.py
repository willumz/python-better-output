import better_output as bo
import time
from better_output import formatting as fmt

a = bo.Output()

a.print("Hello")
time.sleep(1)
a.print("World")
time.sleep(1)
a.output = "World\nHello"
time.sleep(1)
a.insertLine(1, fmt.cyan("Hi"))
