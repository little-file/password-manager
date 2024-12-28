email= input("email/username enter: ")
#password=
def main():
    f = open("passwords.txt", "a")
    f.write(email +  "\n" + password)
    f.close()

main()