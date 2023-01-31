Python 3.11.1 (tags/v3.11.1:a7a450f, Dec  6 2022, 19:58:39) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import re  
... s = 'A message from snehil@google.com to palak@google.com about meeting @2PM'  
... emails = re.findall('\S+@\S+', s)  
... print(emails)  
