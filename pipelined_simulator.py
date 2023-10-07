import time
import threading

def simulate_phase(phase, line_number):
    # The time for each phase (200 ns)
    time.sleep(0.0002)

def simulate_line(line_number):
    # Simulate 5 phases (The taken phases of pipelining)
    for phase in range(1, 6):
        simulate_phase(phase, line_number)

if __name__ == "__main__":
    start_time = time.time()

    inputFile = open("mips_instructions.asm", "r")
    if not inputFile:
        print("Failed to open the file.")
        exit(1)

    lines = inputFile.readlines()
    inputFile.close()

    threads = []
    for line_number, line in enumerate(lines, 1):
        line = line.strip()

        thread = threading.Thread(target=simulate_line, args=(line_number,))
        thread.start()
        threads.append(thread)

    # Finish threads first
    for thread in threads:
        thread.join()

    end_time = time.time()
    print(f"\n\nTime taken by Execution = {(end_time - start_time)} seconds\n\n")
