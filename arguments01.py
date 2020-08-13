import sys

print(sys.argv)
print(len(sys.argv))

if len(sys.argv) < 3:
    print("USAGE: script input_file_path ouput_file_path")
    exit(-1)

else:
    for a in sys.argv:
        print(a)

    input_file_path = sys.argv[1]
    output_file_path = sys.argv[2]

    print(f"Loading {input_file_path}. Emitting to {output_file_path}")
