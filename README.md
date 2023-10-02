# Pipelining vs Non-Pipelining CPU Performance Comparison.

Welcome, in this repository i'm aiming to to compare pipelined and nonpipelined CPU processing.
The objective is to examine how pipelining affects overall processing time.
To keep things simple, I'm not going to build a real simulator that simulates mips (.asm) code processing.


My goal is to write a Python code that presents both the pipelined and non-pipelined techniques after being provided with a python code that generates mips code lines at random. 
Each line in the non-pipelined version takes 800 nanoseconds (0.0008 seconds) to process. 
On the other hand, each phase of processing in the pipelined approach takes 200 nanoseconds (0.0002 seconds).


