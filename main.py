import Function


def choice():
    user = int(input('''\nEnter your Options : 
        1. Get the meaning 
        2. Get the synonym 
        3. Get the antonym 
        4. Get the translation 
        5. Get out
    Enter : '''))
    if user == 5: 
        return False
    else:
        word = input("\nENTER YOUR WORD : ")
        return True, word, user
    


def main():

    condition = True 
    while condition:
        condition, word, user = choice()
        if user == 1: 
            print("\nMeaning of",word, "is : ", Function.get_meaning(word))
            main()
        
        elif user == 2: 
            print("\nSynonym of",word, "is : ", Function.get_synonym(word))
            main()

        elif user == 3: 
            print("\nAntonym of",word, "is : ", Function.get_antonym(word))
            main()
        
        elif user == 4: 
            code = input('Enter your Translation langauge code : ')
            print("\nTranslation of",word, "is : ", Function.translate(word,code))
            main()
        
        elif user == 5: 
            condition = False

        else: 
            print("Invalid input")
            print("TRY AGAIN")
            main()

main()