# Pipelining vs Non-Pipelining CPU Performance Comparison.

Welcome, in this repository i'm aiming to to compare pipelined and nonpipelined CPU processing.
The objective is to examine how pipelining affects overall processing time.
To keep things simple, I'm not going to build a real simulator that simulates mips (.asm) code processing.


My goal is to write a Python code that presents both the pipelined and non-pipelined techniques after being provided with a python code that generates mips code lines at random. 
Each line in the non-pipelined version takes 800 nanoseconds (0.0008 seconds) to process. 
On the other hand, for the pipelined version every line will go through 5 phases (Simulating the 5 phases of pipelining) 
each phase of processing in the pipelined approach takes 200 nanoseconds (0.0002 seconds).


Finally i tried the python code with (100,1000,10000,100000) Lines of mips code, to see how different it'd be
Here's a table showing the results
![image](https://github.com/oAmadu/Pipelining-Comparison/assets/90242708/e7bbe89e-9f1b-49ca-a908-11451c44c323)

![image](https://github.com/oAmadu/Pipelining-Comparison/assets/90242708/db522169-3c0a-4710-b622-8fe3ae25928f)

For smaller lines of code it may seem that it's not that big difference
but we can see how difficult it gets as the code get bigger for the nonpipelined method
While in the pipelined it saves a lot of time
