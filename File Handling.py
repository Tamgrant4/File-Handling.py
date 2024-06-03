# Q1 Task 1

import os

def list_directory_contents(path):
  """Lists all files and subdirectories in the given directory path.

  Args:
      path: The directory path (str).

  Raises:
      OSError: If the specified path is invalid or inaccessible.
  """

  try:
    # Get list of entries in the directory
    entries = os.listdir(path)

    # Print directory heading
    print(f"\nDirectory Listing for: {path}")

    # Iterate and display entries
    for entry in entries:
      # Construct the full path for each entry
      full_path = os.path.join(path, entry)

      # Check if it's a directory using os.path.isdir()
      if os.path.isdir(full_path):
        print(f"[Directory]  {entry}")  # Indicate directories
      else:
        print(f"[File]       {entry}")

  except OSError as e:
    print(f"Error: {e}")  # Print a user-friendly error message

# Get user input for directory path
while True:
  path = input("Enter directory path: ")
  if os.path.exists(path):
    break
  else:
    print("Invalid path. Please enter a valid directory path.")

# Call the function to list contents
list_directory_contents(path)

# Task 2

import os

def report_file_sizes(directory):
  """Reports the sizes of all files in a specific directory.

  Args:
      directory: The directory path (str).

  Raises:
      OSError: If the specified path is invalid or inaccessible.
  """

  try:
    # Get list of entries in the directory
    entries = os.listdir(directory)

    # Iterate through entries
    for entry in entries:
      full_path = os.path.join(directory, entry)

      # Check if it's a file using os.path.isfile()
      if os.path.isfile(full_path):
        # Get file size using os.path.getsize()
        file_size = os.path.getsize(full_path)
        print(f"{entry}: {file_size} bytes")

  except OSError as e:
    print(f"Error: {e}")  # Print a user-friendly error message

# Get user input for directory path
while True:
  path = input("Enter directory path: ")
  if os.path.exists(path):
    break
  else:
    print("Invalid path. Please enter a valid directory path.")

# Call the function to report file sizes
report_file_sizes(path)

# Task 3

import os

def count_file_extensions(directory):
  """Counts and reports the number of files of each extension type in a directory.

  Args:
      directory: The directory path (str).

  Raises:
      OSError: If the specified path is invalid or inaccessible.
  """

  try:
    # Initialize a dictionary to store extension counts
    extension_counts = {}

    # Get list of entries in the directory
    entries = os.listdir(directory)

    # Iterate through entries
    for entry in entries:
      full_path = os.path.join(directory, entry)

      # Check if it's a file using os.path.isfile()
      if os.path.isfile(full_path):
        # Get the extension in lowercase for case-insensitive matching
        extension = os.path.splitext(full_path)[1].lower()

        # Update the count for the extension (create a new key if it doesn't exist)
        extension_counts[extension] = extension_counts.get(extension, 0) + 1

    # Print the file extension counts
    if extension_counts:
      for extension, count in sorted(extension_counts.items()):
        print(f"{extension.upper()}: {count}")  # Print extensions in uppercase
    else:
      print("No files found in the directory.")

  except OSError as e:
    print(f"Error: {e}")  # Print a user-friendly error message

# Get user input for directory path
while True:
  path = input("Enter directory path: ")
  if os.path.exists(path):
    break
  else:
    print("Invalid path. Please enter a valid directory path.")

# Call the function to count extensions
count_file_extensions(path)

# Q 2 Task 1

import re

def extract_emails(filename):
  """Extracts all unique email addresses from a text file.

  Args:
      filename: The path to the text file (str).

  Returns:
      A list of unique email addresses found in the file (list of str).

  Raises:
      OSError: If the file cannot be opened or is inaccessible.
  """

  try:
    # Email address pattern (consider variations and potential special characters)
    email_pattern = r"[a-zA-Z0-9.+_-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"

    # Initialize an empty set to store unique email addresses
    emails = set()

    # Open the file and read its contents
    with open(filename, 'r') as file:
      for line in file:
        # Search for email addresses in the line using re.findall()
        matches = re.findall(email_pattern, line)

        # Add valid matches to the set (avoids duplicates)
        for match in matches:
          emails.add(match)

    # Return the list of unique email addresses
    return list(emails)

  except OSError as e:
    print(f"Error opening file: {e}")
    return []  # Return an empty list on error

# Specify the filename (replace with your actual filename)
filename = "contacts.txt"

# Call the function to extract emails
extracted_emails = extract_emails(filename)

if extracted_emails:
  print("Extracted Email Addresses:")
  for email in extracted_emails:
    print(email)
else:
  print("No email addresses found in the file.")

# Q 3 Task 1

def sentiment_analysis(filename):
  """Analyzes sentiment in travel blog entries and counts positive/negative words.

  Args:
      filename: The path to the text file containing travel blog entries (str).

  Returns:
      A tuple containing the count of positive words and negative words (int, int).
  """

  # Predefined lists of positive and negative words (adjust or expand as needed)
  positive_words = ["amazing", "wonderful", "enjoyed", "breathtaking", "beautiful",
                    "memorable", "unforgettable", "excellent", "fantastic", "stunning",
                    "unique", "enlightening", "delicious", "mesmerizing"]
  negative_words = ["disappointing", "poor", "lackluster", "scarce", "overcrowded", "bad"]

  positive_count = 0
  negative_count = 0

  try:
    with open(filename, 'r') as file:
      for line in file:
        # Convert to lowercase for case-insensitive word matching
        words = line.strip().lower().split()

        # Count occurrences of positive and negative words
        positive_count += sum(word in positive_words for word in words)
        negative_count += sum(word in negative_words for word in words)

  except OSError as e:
    print(f"Error opening file: {e}")
    return 0, 0  # Return 0 for both counts on error

  return positive_count, negative_count

# Specify the filename for the travel blog entries
filename = "travel_blogs.txt"

# Perform sentiment analysis
positive_words, negative_words = sentiment_analysis(filename)

# Print the sentiment analysis report
print(f"Sentiment Analysis Report for Travel Blog Entries:")
print(f"Positive Words: {positive_words}")
print(f"Negative Words: {negative_words}")

if positive_words > negative_words:
  print("Overall sentiment leans towards positive.")
elif positive_words < negative_words:
  print("Overall sentiment leans towards negative.")
else:
  print("Overall sentiment is neutral.")

# Task 2

def sentiment_analysis(filename):
  """Analyzes sentiment in travel blog entries and counts positive/negative words.

  Args:
      filename: The path to the text file containing travel blog entries (str).

  Returns:
      A tuple containing the count of positive words and negative words (int, int).
  """

  # Predefined lists of positive and negative words (adjust or expand as needed)
  positive_words = ["amazing", "wonderful", "enjoyed", "breathtaking", "beautiful",
                    "memorable", "unforgettable", "excellent", "fantastic", "stunning",
                    "unique", "enlightening", "delicious", "mesmerizing"]
  negative_words = ["disappointing", "poor", "lackluster", "scarce", "overcrowded", "bad"]

  positive_count = 0
  negative_count = 0

  try:
    with open(filename, 'r') as file:
      for line in file:
        # Convert to lowercase for case-insensitive word matching
        words = line.strip().lower().split()

        # Count occurrences of positive and negative words
        positive_count += sum(word in positive_words for word in words)
        negative_count += sum(word in negative_words for word in words)

  except OSError as e:
    print(f"Error opening file: {e}")
    return 0, 0  # Return 0 for both counts on error

  return positive_count, negative_count

# Specify the filename for the travel blog entries
filename = "travel_blogs.txt"

# Perform sentiment analysis
positive_words, negative_words = sentiment_analysis(filename)

# Print the sentiment analysis report
print(f"Sentiment Analysis Report for Travel Blog Entries:")
print(f"Positive Words: {positive_words}")
print(f"Negative Words: {negative_words}")

if positive_words > negative_words:
  print("Overall sentiment leans towards positive.")
elif positive_words < negative_words:
  print("Overall sentiment leans towards negative.")
else:
  print("Overall sentiment is neutral.")

