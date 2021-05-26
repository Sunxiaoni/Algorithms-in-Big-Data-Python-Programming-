# Algorithms-in-Big-Data-Python-Programming-
This repository will be updated regularly for my good-practice coding files in terms of algorithms, such as Leetcode, etc.

### Exercise 1

City Council for City 'X' has decided to only give 10 parking passes on a first come basis for a busy street in City 'X'. The parking passes will only be provided on alternate working days of the week (Monday,Wednesday,Friday). Write a function that provides only one parking pass from the below list at a time whenever called in the program. Once a parking pass is issued it cannot be reused.
The check whether the parking pass must be provided or not should be done as decorator function . This decorator function should a importable module function so that it can be reused in other parts of the program.

### Exercise 2

The below code contains an error . Write appropriate comments in the code to explain which line(s) have error and what is the error

class GetterSetter():
    def __init__(self,parameter):
self.parameter = parameter
@property
def parameter(self): return self.parameter
@parameter.setter
def parameter(self,value): self.parameter = value
obj = GetterSetter(1)

### Exercise 3

City Council for City 'X' has decided to test recovered patients of COVID-19 so that it can safely confirm that patients cured of the virus are not getting infected again. Given the huge number of tests City 'X' needs to do on all its inhabitants, the council has decided not to test all recovered patients but instead choose 1 random recovered patients in every recoverd patient 5 . The list of the recovered patients is as below and can grow in future. The below list can be hard coded in your program:
['p1','p2','p3','p4','p5','p6','p7','p8','p9','p10','p11','p12','p13','p14','p15', 'p16','p17','p18','p19','p20']

The batch size of 5 can change depending on whether City 'X' wants to do more or less testing. Before choosing the next patient, City 'X' also needs to record the test date as its an important paramter to know when the patient was tested. Only print the test date in your program
Write an object-oriented python program that helps City 'X' choose recovered patients for testing.

### Exercise 4

The below code contains a logical error and prints 'None'. Make changes in the code to print 'from 3'

def function1(value):
    return value
def function2(func):
    func()
def function3(): return 'from 3'
print(function1(function2(function3)))

### Exercise 5

One vital part of Smart City are hospitals . How would you model hospitals in object oriented python programming ?
All Hospitals must contain atleast 15 beds . The number of beds should be allowed to modified if in future we plan to reduce or increase the minimum bed condition. Each hospital must contain: name
number of doctos
numbers of nurses
medical speciality it caters to (for eg hospital A caters to : orthopedic, cardiac and hospital B caters to general medicine and neurosurgery).
Each of the above property can change. Medical speciality can be added to hospitals but existing ones cannot be removed or modified.

### Exercise 6

Email address provide a lot of information in terms of domains and sub domains. Write a python function that expects a email address as input and gets decorated with two extractor function : one for domain extraction
and the other for subdomain extraction
Once extracted only print the domain, sub domain name

### Exercise 7

Game Mechanics: The game is a card game between two entities. The game can be played between two humans or a human and a machine. Choose a set of characters(fictional or real) and their characteristics. Characteristics are represented by a specific numeric value indicating the strength of the characteristic (strength may be indicated by negative or positive numeric value). Each card contains only one character and its characteristics.
Characteristics must be same across all characters but can vary in strength. No characteristic across characters can share the same value.
The two entities will be called Player 1 and Player 2 hence.
Distribute the cards equally among player 1 and player 2 face down such that the players cannot see the characters they have been given. Simulate a dice throw by both player 1 and player 2 where the highest number starts first
Constraints : Each player gets two special spells (God and Resurrect) . These spells are not associated to the characters but is assoicated to the player itself
Each round is played as below:
Player 1 : chooses the first card from the deck and can : play a charactertistic he wishes to challenge player 2 with . Player 2 chooses the first card in his deck and compares the charactertistic. The round is won by the Player whose characteristic weighs more and gets 1 point. The 2 cards are then kept faced down on a different deck called 'outdated'(the cards in the outdated deck are schuflled in a random order after each card is placed). In round 2 , The player who won the previous round begins by choosing the next card in his deck and the round proceeds as above.
Spells:
In each round a player can decide to play the God spell or the Resurrect spell along with challenging with a characteristic.
God Spell: The player who starts the round must choose the next card and characteristic on his deck. After choosing he can play the God spell, forcing the opponenet player to play any card that he chooses. The game proceeds with the comparision of the the charactestic on the choosen card.
Resurrect Spell: Before choosing the next card and characteristic, the player who starts the round can choose Resurrect spell. Choosing Resurrect will create a random number and the card at the that random number position from the 'outdated' deck will be choosen. The card present at the random number at the 'outdated' deck will be added back to the top of the player deck. The player must then play this card.
When Player 1 plays the God spell , Player 2 cannot play the God spell as he is forced to choose the card, however player 2 can play the Resurrect spell and add a new card to the top of his deck. Player 1 can then force the resurrected card to be choosen or can go with his earlier choice.
God and Resurrect spell can only be played once by each Player.
The Game ends when all cards of one / both players have been played.
The game is won by the player with maximum points.
Please note : the game mechanics is not perfect and can imbalence the game , but for the purpose of this exercise that can be overlooked.

### Exercise 8

Write a function that takes two string S1 and S2 at its input and returns a boolean denoting whether S2 matches / contains S1. (avoid using python regex or in build python regex matching features)
S1 is a sequence of: a-z - which stands for itself
S2 is a sequence of any number of the following:
a-z - which stands for itself
.(dot) - which matches 1 occurrence of any character
*(star)- which matches 0 or more occurrences of the previous single character
Examples:
S1 = "aba" , S2 = "*ab" => false
S1 = "aa" , S2 = "a*" => true
S1 = "ab" , S2 = ".*" => true
S1 = "ab", S2 = "." => false
S1 = "aab" , S2 = "c*a*b" => true S1 = "aaa" , S2 = "a*" => true

### Exercise 9

Development and enhancement of the performance of python library GNE in terms of input argument change from HTML to URL, implementation of asyncio for performance improvement.

