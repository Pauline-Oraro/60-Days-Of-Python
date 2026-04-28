print("WEBSITE URL CHECKER")
url = input("Enter the URL of the website you want to check: ")

# we will use the if elif else statement to check if the URL starts with "https://" or "http://"
if url.startswith('https://'):
    print("This website uses HTTPS which is secure.")
elif url.startswith("http://"):
    print("This website uses HTTP which is not secure.")
else:
    print("Invalid URL. Please make sure to include http:// or https://")

# in the terminal, you can run this code and input a website URL to check if it is secure or not.
# Example:
# Enter the URL of the website you want to check: https://github.com/Pauline-Oraro
# This website uses HTTPS which is secure.