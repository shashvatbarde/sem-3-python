import re
def find_emails(filename):
    file = open(filename, "r")
    text = file.read()
    file.close()
    pattern = r'[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}'
    emails = re.findall(pattern, text)
    return emails
# Main program
filename = input("Enter the text file name: ")
emails = find_emails(filename)
print("Email addresses found:")
for email in emails:
    print(email)