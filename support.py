def welcome():
    print('Welcome to the automated technical support system.')
    print('Please describe your problem:')

def get_input():
    return input().lower()

def dictionary(word):
    dict_1 = {"crashed":"Are the drivers up to date?", "blue":"Ah, the blue screen of death. And then what happened?", "hacked":"You should consider installing anti-virus software.", "bluetooth":"Have you tried mouthwash?", "windows":"Ah, I think I see your problem. What version?", "apple":"You do mean the computer kind?", "spam":"You should see if your mail client can filter messages.", "connection":"Contact Telkom."}
    if word in dict_1:
        return dict_1[word]
    else:
        return "Curious, tell me more."
        

def main():
    welcome()    
    query = get_input()
    
    while (not query == "quit"):
        print(dictionary(query))

        query = get_input()    

if __name__=='__main__':
    main()