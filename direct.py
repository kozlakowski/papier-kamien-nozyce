import pyperclip

print("Enter username")
username = input()


print("Directory is: ")
new = "www/{}.server691.seedhost.eu/{}/rutorrent/share/users/{}/settings/".format(username, username, username)
pyperclip.copy(new)
print(new)
