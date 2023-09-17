#case insensitive counting
freq={}
s=input("Enter the Sentence: ").lower()
words=s.split()
for i in words:
    i=i.strip(".,!?()[]{}:;\"'")
    if i in freq:
        freq[i]+=1
    else:
        freq[i]=1
print("The Frequecy of Each Words are:")
for k,v in freq.items():
    print(k,":",v)
