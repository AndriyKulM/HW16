from ipaddress import ip_address
import re


# 1. Search a phone numbers

pattern1 = r"\d{1,3}[-]\d{1,3}[-]\d{1,4}"          # \d - all digits
text1 = "Hello, my phone number is 251-65-23."

result_phone = re.findall(pattern1, text1)

if result_phone:
    print(result_phone)
    print("Phone number found!")
else:
    print("Phone number not found!")


# 2. Basic validation for email
    """
    Local part should be consisted of lower/upper case, number,
    underscore and dot. Domain part - the same
    but dot symbol could not be the first character
    """

pattern2 = r"[\w.]+@[\w]+[.\w]+"              #  \w - equivalent to [a-zA-Z0-9_]
text2 = "John.Smith_1234@gmail.com"

result_email = re.match(pattern2, text2)

if result_email:
    print(result_email[0])
    print("Email is valid!")
else:
    print("Wrong email!")


# 3. Remove redundant zeros from an IP address

text3 = "206.0.094.006"
octets = re.split(r"\.", text3)               # breaking the ip address into octets
octets = [int(octet) for octet in octets]     # convert to an integer to remove redundant zeros
octets = [str(octet) for octet in octets]     # back to string
result_rrz = ".".join(octets)                 # and join octets into ip address by separator '.'
print(result_rrz)


# 4. Check if IP address is valid

ip_address_ = "216.8.94.196"
pattern3 = r"^\d+\.\d+\.\d+\.\d+$"

# check whether the octet is in the range from 0 to 255 and whether there are 4 octets
result_ip = [0<=int(octet)<256 for octet in re.split("\.", re.match(pattern3, ip_address_).group(0))].count(True)==4
if result_ip==True:
    print("ip address is valid!")
else:
    print("invalid ip address")
