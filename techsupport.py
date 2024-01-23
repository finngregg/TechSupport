def welcome():
    print('Welcome to the automated technical support system.')
    print('Please describe your problem:')

def get_input():
    return input().lower()

def dictionary(sen):
    dict_1 = {"crashed":"Are the drivers up to date?", "blue":"Ah, the blue screen of death. And then what happened?", "hacked":"You should consider installing anti-virus software.", "bluetooth":"Have you tried mouthwash?", "windows":"Ah, I think I see your problem. What version?", "apple":"You do mean the computer kind?", "spam":"You should see if your mail client can filter messages.", "connection":"Contact Telkom."}
    k = 0
    for x in sen:
        if x in dict_1:
            k=x
            break
    if k==0:
        return "Curious, tell me more."
    else: 
        return dict_1[k]
    

def main():
    welcome()    
    query = get_input().split()
    
    while query[0]!="quit":
        print(dictionary(query))

        query = get_input().split()   

if __name__=='__main__':
    main()