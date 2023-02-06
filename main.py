# Create a list of characters using list comprehension
char_list = [ char for char in "linuxhint" ]
print (char_list)

# Define a tuple of websites
websites = ("google.com", "yahoo.com", "ask.com", "bing.com")

# Create a list from tuple using list comprehension
site_list = [ site for site in websites ]
print(site_list)





#buidling ML Model for breast cancer data

#importing the libraries

df= pd.read_csv("Cancer.csv")

df.head()