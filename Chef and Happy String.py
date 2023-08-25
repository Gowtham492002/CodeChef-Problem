def is_happy_substring(s):
    vowels = "aeiou"
    count = 0
    for char in s:
        if char in vowels:
            count += 1
            if count > 2:
                return True
        else:
            count = 0
    return False

def main():
    t = int(input())
    for _ in range(t):
        s = input().strip().lower()  
        if is_happy_substring(s):
            print("HAPPY")
        else:
            print("SAD")

main()
