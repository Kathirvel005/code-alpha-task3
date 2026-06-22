# Task Automation with Python Scripts
# Extract email addresses from a text file and save them to another file

import re

# Input and output file names
input_file = "input.txt"
output_file = "emails.txt"

try:
    # Read content from input file
    with open(input_file, "r") as file:
        content = file.read()

    # Find all email addresses using regex
    emails = re.findall(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", content)

    # Save extracted emails to output file
    with open(output_file, "w") as file:
        for email in emails:
            file.write(email + "\n")

    print(f"Successfully extracted {len(emails)} email(s).")
    print(f"Saved to '{output_file}'.")

except FileNotFoundError:
    print(f"Error: '{input_file}' not found.")
