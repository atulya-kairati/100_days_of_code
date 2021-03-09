HANGMANPICS = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

#Word bank of animals
words = ('ant baboon badger bat bear beaver camel cat clam cobra cougar '
         'coyote crow deer dog donkey duck eagle ferret fox frog goat '
         'goose hawk lion lizard llama mole monkey moose mouse mule newt '
         'otter owl panda parrot pigeon python rabbit ram rat raven '
         'rhino salmon seal shark sheep skunk sloth snake spider '
         'stork swan tiger toad trout turkey turtle weasel whale wolf '
         'wombat zebra ').split()

banner = r'''
  o         o           o           o          o        o__ __o       o          o           o           o          o  
 <|>       <|>         <|>         <|\        <|>      /v     v\     <|\        /|>         <|>         <|\        <|> 
 < >       < >         / \         / \\o      / \     />       <\    / \\o    o// \         / \         / \\o      / \ 
  |         |        o/   \o       \o/ v\     \o/   o/               \o/ v\  /v \o/       o/   \o       \o/ v\     \o/ 
  o__/_ _\__o       <|__ __|>       |   <\     |   <|       _\__o__   |   <\/>   |       <|__ __|>       |   <\     |  
  |         |       /       \      / \    \o  / \   \\          |    / \        / \      /       \      / \    \o  / \ 
 <o>       <o>    o/         \o    \o/     v\ \o/     \         /    \o/        \o/    o/         \o    \o/     v\ \o/ 
  |         |    /v           v\    |       <\ |       o       o      |          |    /v           v\    |       <\ |  
 / \       / \  />             <\  / \        < \      <\__ __/>     / \        / \  />             <\  / \        < \ 
'''