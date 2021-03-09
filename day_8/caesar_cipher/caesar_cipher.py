print('''
    ><<          ><        ><<<<<<<<   ><< <<         ><        ><<<<<<<    
 ><<   ><<      >< <<      ><<       ><<    ><<      >< <<      ><<    ><<  
><<            ><  ><<     ><<        ><<           ><  ><<     ><<    ><<  
><<           ><<   ><<    ><<<<<<      ><<        ><<   ><<    >< ><<      
><<          ><<<<<< ><<   ><<             ><<    ><<<<<< ><<   ><<  ><<    
 ><<   ><<  ><<       ><<  ><<       ><<    ><<  ><<       ><<  ><<    ><<  
   ><<<<   ><<         ><< ><<<<<<<<   ><< <<   ><<         ><< ><<      ><<
                                                                            
      ><<    ><< ><<<<<<<   ><<     ><< ><<<<<<<< ><<<<<<<                  
   ><<   ><< ><< ><<    ><< ><<     ><< ><<       ><<    ><<                
  ><<        ><< ><<    ><< ><<     ><< ><<       ><<    ><<                
  ><<        ><< ><<<<<<<   ><<<<<< ><< ><<<<<<   >< ><<                    
  ><<        ><< ><<        ><<     ><< ><<       ><<  ><<                  
   ><<   ><< ><< ><<        ><<     ><< ><<       ><<    ><<                
     ><<<<   ><< ><<        ><<     ><< ><<<<<<<< ><<      ><<              
                                                                            
''')


def shift(letter, key):
    asc = ord(letter)
    return chr(asc + key) if 97 <= asc + key <= 122 else chr(96 + (asc + key - 122)) if asc + key >= 97 else chr(26 + asc + key)


def encode(word, key):
    return ''.join([shift(letter, key) for letter in word])


def decode(word, key):
    return ''.join([shift(letter, -key) for letter in word])


def main():
    choice = input('Enter encode or decode to choose: ')
    string = input(f'Enter the word to be {choice}d: ')
    key = int(input('Enter the Key or the shift number: '))

    if choice == 'encode':
        print(encode(string, key))
    elif choice == 'decode':
        print(decode(string, key))
    else:
        print('Wrong Choice Dumbass!!')


if __name__ == '__main__':
    main()


