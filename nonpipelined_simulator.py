import time

def simulate_time():
    time.sleep(0.0008)

if __name__ == "__main__":
    start_time = time.time()

    inputFile = open("mips_instructions.asm", "r")
    if not inputFile:
        print("Failed to open the file.")
        exit(1)

    # Process the file
    for line in inputFile:

        # Sleep for 800 nanoseconds
        simulate_time()

    inputFile.close()

    end_time = time.time()
    print(f"\n\nTime taken by Execution = {(end_time - start_time)} seconds\n\n")
