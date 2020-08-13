try:
    f = open("hope.txt", "r")
    all = f.readlines()
    for line in all:
        print(line.strip('\n'))
    f.close()

except:
    print("File not found or can’t be read.")

finally:
    print("Cleaning Up")

print("Finished")
