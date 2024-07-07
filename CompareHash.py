"""Compare Hashes python script"""

Hash1 = input("please enter your first hash: ")
Hash2 = input("please enter your second hash: ")

Hash1Lower = Hash1.lower()
Hash2Lower = Hash2.lower()

if Hash1Lower == Hash2Lower:
	print("Hashes Match")
else:
	print("Warning!!!\nHashes do not match")

print("program has completed have a nice day")
 


