#case insensitive 
freq={}
with open(r"C:\Users\gauth\AppData\Local\Programs\Python\Python311\myfile.txt","r") as f:
    content=f.read().title()
    wlist=content.split()
    for i in wlist:
        i=i.strip(".,!?()[]{}:;\"'")
        if i in freq:
            freq[i]+=1
        else:
            freq[i]=1
f.close()
freq=dict(sorted(freq.items(),key=lambda i: i[1], reverse=True))
print("Words And Frequency in reverse Order: ")
for k,v in freq.items():
    print(k,":",v)
