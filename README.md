# TechSupport
 
# somehelp.py 

A program that randomly selects a response from a list. The list contains the following responses in the following order:

1. Have you tried it on a different operating system?
2. Did you reboot it?
3. What colour is it?
4. You should consider installing anti-virus software.
5. Contact Telkom.
6. I should get that looked at if I were you.

# support.py 

A modified version of somehelp.py that keeps a dictionary of responses indexed by keywords.

- Assume that the user only ever inputs a single word at a time.
- Given a word entered by the user, the program will look for that entry in the dictionary and
will print the associated response.
- If there is no entry for that word the program will output 'Curious, tell me more.'.

# techsupport.py 

A modified version of support.py that splits a query up into a list of words and then, taking each in turn,
searches the dictionary for a match.

- Once it finds a match it should print the associated response.
- It should NOT print more than one response.
- If none of the words can be matched then the program should output 'Curious, tell
me more.'.