#!/usr/bin/env python
#
# Note: This is basically what's happening here.
# 1: Hash the inputstring to sha1
# 2: Make the hash into an UPPERCASE string!
# 3: Go through each line of the dump file, and check for match
# 4: If found, return or present the number after the colon (:),
#       which represents the number of occurences in the HIBP database.

import os
import hashlib
from pyspin.spin import make_spin, Box1
import argparse
import sys


def make_uppercase_hash_string(input):
	# Firstly hashlib only wants bytes, so we convert the input string to bytes.
	bytes_to_hash = input.encode()

	# Next we let the sha1() function in hashlib give us the hash. It will return a <class '_hashlib.HASH'>.
	hash_object = hashlib.sha1(bytes_to_hash)

	# Next we convert the <class '_hashlib.HASH'> object into a string of the hash.
	hex_dig = hash_object.hexdigest()

	# Now we need the previous string uppercased, to match the format in the dump file.
	hash_string = hex_dig.upper()

	# Lastly we'll return the string with the uppercased hash.
	return hash_string


@make_spin(Box1, "Looking for hash in dump...")
def process_for_tty(filename, string_to_find):
	# Here we step through the dump file, looking for a match.
	# First we take our string_to_find and get it converted to a hash string.
	print("Password to look for: " + string_to_find)
	hash_to_find = make_uppercase_hash_string(string_to_find)
	print("Hash of the password: " + hash_to_find)
	print("Filename of dumpfile: " + filename)

	# Next we open the dump file read-only
	with open(filename, 'r') as dump:
		# Now we'll go through each line in the dump file, looking for a match with our hash_to_find.
		for line in dump:
			if str(hash_to_find).upper() in line:
				# If there's a match, just print it to the terminal. The program is done at that point, and we can quit.
				# Notice that we print the entire line, we found the hash in. But we cut everything before the colon (:)
				# This way we will only get a string with the number of occurences.
				print("\n Number of occurences: " + str(line).split(":")[1])
				quit()
	# In case there are no matches, we just print a fitting message, and break out of this function.
	print("\n Found 0 occurences of this password")


def process_for_nontty(filename, string_to_find):
	# Here we process it, as if it weren't  a tty. Meaning we only return the number of occurences.
	# First we take our string_to_find and get it converted to a hash string.
	hash_to_find = make_uppercase_hash_string(string_to_find)

	# Next we open the dump file read-only
	with open(filename, 'r') as dump:
		# Now we'll go through each line in the dump file, looking for a match with our hash_to_find.
		for line in dump:
			if str(hash_to_find).upper() in line:
				# If there is a match, we immediately return the number after the colon (:),
				#   on the line, the hash was found.
				return str(line).split(":")[1]
	# We'll reach this line of there is no match. We therefore simply return a 0.
	return 0


if __name__ == '__main__':
	# First we handle the command line arguments, and assign the parameters to simple variables.
	argumentparser = argparse.ArgumentParser(
						description="HasThisBeenPwned - Checks if a string has been used as a password in a HIBP dump.")
	argumentparser.add_argument('input', type=str,
						help='The password you want to check.')
	argumentparser.add_argument('-filename', type=str,
								help='Optional: Absolute path to a pwned-passwords-sha1-ordered-by-hash-v6.txt file.',
								default='pwned-passwords-sha1-ordered-by-hash-v6.txt')
	args = argumentparser.parse_args()
	arg_string_to_check = args.input
	arg_filename = args.filename

	# Next we determine if this script is called from a tty.
	# If it is, we can give the user "pretty output.
	# If it's not, the scripts output is probably being piped to another program. So we'll just return the result.
	#
	# Additionally we'll wrap the whole thing in a try/except to handle KeyboardInterrupt and SystemExit (ctrl+c)
	# We'll specifically use os._exit(1) to give a return code of 1, because the "with open()" thingy locks the thread.
	# If this isn't dealth with by os._exit(), and exception will be thrown, because the lock termination isn't handled.
	try:
		if sys.stdout.isatty():
			process_for_tty(arg_filename, arg_string_to_check)
		else:
			process_for_nontty(arg_filename, arg_string_to_check)
	except (KeyboardInterrupt, SystemExit):
		os._exit(1)
