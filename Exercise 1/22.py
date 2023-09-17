s1=input("Enter the First word: ")
s2=input("Enter thr Second word: ")
if len(s1)!=len(s2):
    print(f"{s1} and {s2} are not Anagram")
else:
    if sorted(s1.lower())==sorted(s2.lower()):
        print(f"{s1} and {s2} are Anagram")
    else:
        print(f"{s1} and {s2} are not Anagram")
