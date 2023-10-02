# Pipelining vs Non-Pipelining CPU Performance Comparison.

Welcome, in this repository i'm aiming to make a comparison between pipelined/nonpipelined CPU processing.
The goal is to analyze the impact of pipelining on overall processing time.
to make it simple to understand i'm not going to make an actual simulator that simulates mips (.asm) code processing.

I'm provided with a python code that randomly generates mips code lines, here comes my work to make some python code that represents both the pipelined and non-pipelined approaches. 
In the non-pipelined approach, each line takes 800 nanoseconds (0.0008 seconds) for processing. 
Conversely, in the pipelined approach, each phase of processing takes 200 nanoseconds (0.0002 seconds).
