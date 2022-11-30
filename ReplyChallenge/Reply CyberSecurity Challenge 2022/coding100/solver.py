from functools import lru_cache
import numpy as np

def find_horizontal(word, grid):
    for y, line in enumerate(grid):
        linestr = "".join(line)
        index = linestr.find(word)
        if index == -1:
            index = linestr.find(word[::-1])

        if index != -1:
            grid[y][index:index+len(word)] = [' ']*len(word)
            return True    
    return False

def find_diagonal(word, grid):
    print("\nRunning for word:", word)
    startings = []
    for y, line in enumerate(grid):
        for x, letter in enumerate(line):
            if letter == word[0]:
                if x > 0 and y > 0 and grid[y-1][x-1] == word[1]:
                    startings.append((x, y, -1, -1))
                elif x > 0 and y < len(grid)-1 and grid[y+1][x-1] == word[1]:
                    startings.append((x, y, -1, 1))
                elif x < len(line)-1 and y > 0 and grid[y-1][x+1] == word[1]:
                    startings.append((x, y, 1, -1))
                elif x < len(line)-1 and y < len(grid)-1 and grid[y+1][x+1] == word[1]:
                    startings.append((x, y, 1, 1))
                
    print(startings)
    for sx, sy, dx, dy in startings:
        try:
            linestr = "".join([grid[sy+dy*i][sx+dx*i] for i in range(len(word))])
            print(linestr)
        except:
            continue
        if word == linestr:
            for i in range(len(word)):
                grid[sy+dy*i][sx+dx*i] = ' '
            return True
    
    return False


if __name__ == "__main__":

    grid = []
    words = []

    with open('challenge.txt') as file:
        lines = file.readlines()
        for line in lines[1:46]:
            grid.append(line.strip().split())

        words = [word.strip() for word in lines[49:199]]

    # remove horizontals
    remaining_words = []

    for word in words:
        found = find_horizontal(word, grid)
        if not found:
            remaining_words.append(word)

    words = remaining_words
    remaining_words = []

    # remove verticals
    # transpose grid and remove horizontal, then transpose again
    grid = np.array(grid).T.tolist()
    for word in words:
        found = find_horizontal(word, grid)
        if not found:
            remaining_words.append(word)

    grid = np.array(grid).T.tolist()

    words = remaining_words
    remaining_words = []

    for word in words:
        found = find_diagonal(word, grid)
        if not found:
            remaining_words.append(word)

    words = remaining_words
    remaining_words = []


    # avoid L-shape step, do by hand

    for line in grid:
        line = " ".join(line)
        print(line)

    print('\n')

    for word in words:
        print(word)

    """
    RESULT IS THIS:

              F               Z R Q E A C A               J L W F S E V E R A L Y Y N V R
                  R   F                 V C C                   P U W T               M I
                  S   Z N L E R U T X I M C V I J H N X U S U R P A T E D                
                  E   T X W U E C N A T P E R A P P R O A C H R U E I R E D O P H P H   M
  M D K W Y O     S   M R E L L A M S Y H B U Z   G H G V V I E F Z O R R N L   B T J   S
    A M F M O     C   P Y                   E A   N G D B B N T C W N I E T X   B U     Q
  P   Z O J O     A   X A               E D R S   I N Z X B G S Q M D B E I Z   O I     U
  A     O A P     R   T R A V E L E D O   W L C   L W J   E I O L V H L H G O           C
      W   O Z     C               D       Q   Y   L D T     C O R W Q E C I N           Q
        X   I     E O I R A O R P U       H   F   I F W       R                          
K       D         L U E K A T S I M       L       K   R N       F Z F B     T            
J       E   K   J Y S H E L P L E S       S       J P   E N       U Z V       E          
N       S   K X   L L S A J Z C A S       Z     W S B     W         C F       L     C    
C       E     J Z   Y L A F M S N L               T Y   A   U         G       B     L    
    F   R                         Y               W F   T D   Q       G       A     S    
D   W   V                     E W J Y Q Z         L A     E                   N   M N    
  X   J E       Y I               E S I           K S     N           O       O   K      
        D       L                 X T N             H     R     H       C A   S   C   B Y
      V   N     T O                 R               I     U     F         L   A   I      
      P R       H Y O B E D I E N T O               O S   T         P J     P E   W      
      O G P     G F S C O N S I D E K               N     E         G U L   M R   P      
      R B Q A   I S I L B T A U S R I     N         P     R         K   C K   M   M      
      P F F K C R W D J N A T Y P E N     T N   K   T                   C E Y     A      
      O   M K O R               N D G     S M           E               G X A E I L      
D E D I                 B L E S S E D   B O G     A     T               S P E R I N G    
S P E S   L K B T J E N O R M O U S Z   O M A     M     E     X         I T R E M E N D  
B B T E   U                               N C     M     R     U U       H P S R   R O O  
S N S T   F O Q H N D                             N     N     Y M       W   R S   X B U  
H   E V   D A B A N D O N E D R E M E M B E R E   V     A     F U           E C   P   S  
A   G A   A S A T R O F M O C T G M U P B M Y S   X     L       K     T     S     P   V  
R   I D   E S B B H                   A K   O D T R   P Y E     H     M     O         Z  
P   D H   R E L M                   P T   T                       E   F     U         F  
L   E H T D L E R S                   R         B V O C J S     I   N O     R         P  
Y   U   A   E H T R E V E N V F D C N I R         Q Y O N H       D   Y     C            
    X   O   K N O B I               U O W E         H I P I       G G       E           Z
        C   H X Z               Z B H T   A T         E G F       Z U T   I E           M
  K     T   Y                         I     Z R         N T   B     E E     Q M         Z
        S   L C U T X   E R K A V A Q C B     H A       M I   V   S     K     X          
        I   E Q G W L C                         K U   T   N   F   U X           U W      
        A   T E L P M O C   Z E X E C U T I O     Q Q   K G   O   S D E           G      
        W                                   N E     C L I Z A T I O N P O         G      
                      K B V Q   U B K S M O E J N     I V D E H S I N R U F              
      M H X F                 J   V S U B H R P X Z   V R T D               G         U  
Z     J I                 C W B Q   A R               I Z                   Y M M     K  
N L   S D C H Y Z X                   R O U N D E D S C                                  


*CIVILIZATION
*UPROARIOUSLY
*COMPLETELY
*DISOBEDIENT
*EXECUTIONER
*HELPLESSLY
*CONSIDERED
*TREMENDOUS
*USURPATION
*ACCEPTANCE
*COMFORTABLE
*APPROACHING
*NEVERTHELESS
*SURROUNDED
*WHISPERING

    THAT BECOMES THIS AFTER REMOVING THE OTHER WORDS IN L SHAPE

              F               Z R Q E A C                 J L W F S E V E R A L Y Y N V R
                  R   F                 V   C                   P U W T               M I
                  S   Z N L E R U T X I M   V I J H N X               E D                
                  E   T X W U               R                 R U E   R E D O P H P H   M
  M D K W Y O     S   M R E L L A M S Y H B U Z   G H G V V   E F Z   R R N L   B T J   S
    A M F M O     C   P Y                   E A   N G D B B   T C W   I E T X   B U     Q
  P   Z O J O     A   X A               E D R S   I N Z X B   S Q M D B E I Z   O I     U
  A     O A P     R   T R A V E L E D O   W L C   L W J   E I O L V H L H G O           C
      W   O Z     C               D       Q   Y   L D T     C O R W Q E C I N           Q
        X   I     E                       H   F   I F W       R                          
K       D         L   E K A T S I M       L       K   R N       F Z F B     T            
J       E   K   J Y                       S       J P   E N       U Z V       E          
N       S   K X   L   S A J Z C A         Z     W S B     W         C F       L     C    
C       E     J Z     L A F M S N                 T Y   A   U         G       B     L    
    F   R                                         W F   T D   Q       G       A     S    
D   W   V                     E W J Y Q Z         L A     E                   N   M N    
  X   J E       Y I               E S I           K S     N           O       O   K      
        D       L                 X T N             H     R     H       C A   S   C   B Y
      V   N     T O                 R               I     U     F         L   A   I      
      P R       H Y                 O               O S   T         P J     P E   W      
      O G P     G F                 K               N     E         G U L   M R   P      
      R B Q A   I S   L B T A U S   I     N         P     R         K   C K   M   M      
      P F F K C R W   J N A T Y P   N     T N   K   T                   C E Y     A      
      O   M K O R               N   G     S M           E               G X A E I L      
D E D I                 B L E S S E D   B O G     A     T                               
S P E S   L K B T J E N O R M O U S Z   O M A     M     E     X                          
B B T E   U                               N C     M     R     U U         P S R   R O    
S N S T   F O Q H N D                             N     N     Y M           R S   X B    
H   E V   D A B A N D O N E D R E M E M B E R E   V     A     F U           E C   P      
A   G A   A                   T G M U P B M Y S   X     L       K     T     S     P   V  
R   I D   E     B H                   A K   O D T R   P Y E     H     M     O         Z  
P   D H   R     M                   P T   T                       E   F     U         F  
L   E H T D     R S                   R         B V O C J S     I   N O     R         P  
Y   U   A                   V F D C N I R         Q Y O N H       D   Y     C            
    X   O   K N O B I               U O W E         H I P I       G G       E           Z
        C   H X Z               Z B H T   A T         E G F       Z U T   I E           M
  K     T                             I     Z R         N T   B     E E     Q M         Z
        S     C U T X   E R K A V A Q C B     H A       M I   V   S     K     X          
        I     Q G W L C                         K U   T   N   F   U X           U W      
        A                   Z                     Q Q   K G   O   S D E           G      
        W                                     E     C                 P O         G      
                      K B V Q   U B K   M O   J N       V D E H S I N R U F              
      M H X F                 J   V S   B H   P X Z     R T D               G         U  
Z     J I                 C W B Q   A                   Z                   Y M M     K  
N L   S D C H Y Z X                                 S                                    


    WHICH FLATTENED IS THE PASSWORD:

FZRQEACJLWFSEVERALYYNVRRFVCPUWTMISZNLERUTXIMVIJHNXEDETXWURRUEREDOPHPHMMDKWYOSMRELLAMSYHBUZGHGVVEFZRRNLBTJSAMFMOCPYEANGDBBTCWIETXBUQPZOJOAXAEDRSINZXBSQMDBEIZOIUAOAPRTRAVELEDOWLCLWJEIOLVHLHGOCWOZCDQYLDTCORWQECINQXIEHFIFWRKDLEKATSIMLKRNFZFBTJEKJYSJPENUZVENSKXLSAJZCAZWSBWCFLCCEJZLAFMSNTYAUGBLFRWFTDQGASDWVEWJYQZLAENMNXJEYIESIKSNOOKDLXTNHRHCASCBYVNTORIUFLAIPRHYOOSTPJPEWOGPGFKNEGULMRPRBQAISLBTAUSINPRKCKMMPFFKCRWJNATYPNTNKTCEYAOMKORNGSMEGXAEILDEDIBLESSEDBOGATSPESLKBTJENORMOUSZOMAMEXBBTEUNCMRUUPSRROSNSTFOQHNDNNYMRSXBHEVDABANDONEDREMEMBEREVAFUECPAGAATGMUPBMYSXLKTSPVRIDEBHAKODTRPYEHMOZPDHRMPTTEFUFLEHTDRSRBVOCJSINORPYUAVFDCNIRQYONHDYCXOKNOBIUOWEHIPIGGEZCHXZZBHTATEGFZUTIEMKTIZRNTBEEQMZSCUTXERKAVAQCBHAMIVSKXIQGWLCKUTNFUXUWAZQQKGOSDEGWECPOGKBVQUBKMOJNVDEHSINRUFMHXFJVSBHPXZRTDGUZJICWBQAZYMMKNLSDCHYZXS
    """