

def interger(string, N):
    if len(string) == N: # if the length of the string is equal to N 
        print(string)
    elif len(string) > N:
        print(string[:N]) # if the length of the string is greater than N slice the string to the size of N
    elif len(string) < N:
        string_count = N // len(string)
        remainder = N % len(string)
        size_string = string * string_count + string[:remainder]
        print(size_string)        

interger("abc" ,3)
interger("abcde" ,5)
interger("abcdef",30)