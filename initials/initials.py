def get_initials(fullname):
   # my_name =("")
    name_list= fullname.split()
    initials=("")
    for name in name_list:
        initials=initials+name[0].upper()   
    return initials
def main():
    res=get_initials("kavitha sridhar")
    print(res)
if __name__ == '__main__':
    main() 
 