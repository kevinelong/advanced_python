import sys

try:
    f = open("hope2.txt", "r")
    all = list(f.readlines())
#
# except OSError as err:
#     print(f"SSS OS error: {err}")
#     raise
#
# except ValueError:
#     print("Could not convert data to an integer.")

except:
    print("Unexpected error:", sys.exc_info()[0])
    # raise

finally:
    print("Cleaning Up")
    if "f" in globals():
        f.close()

if "f" in globals():

    for line in all:
        print(line.strip('\n'))
    print("Finished")

