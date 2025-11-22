#num=input("Enter the number to check if palindome:")
def is_palindrome(num):
    str_num=str(num)
    rev_str_num=str_num[::-1]
    if str_num==rev_str_num:
        return True
    else:
        return False

if __name__=="__main__":
    lst=[]
    for k in range(10,1000):
        if is_palindrome(k):
           lst.append(k) 
    print("The palindrome numbers between 0 and 1000 are:",lst)