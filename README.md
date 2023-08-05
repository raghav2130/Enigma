# Enigma

Well those who don't know .. 

 # TL;DR
 
The Enigma machine was a cryptographic device used to encrypt and decrypt secret messages during World War II and beyond.
The Enigma machine was invented by the German engineer Arthur Scherbius in the early 20th century and was later adopted by various military and government organizations for secure communication.
The encryption mechanism of the Enigma machine was based on a combination of electrical pathways, rotating wheels (rotors), and a reflector. When a key on the keyboard was pressed, an electrical signal passed through the rotors, causing them to rotate and create a unique electrical circuit for each letter. This circuit scrambled the plaintext letter into a corresponding cipher letter. After passing through the rotors, the signal was then reflected back through a fixed reflector, further encrypting the letter. The use of multiple interchangeable rotors and secret daily key settings made the Enigma machine extremely complex and 'Impossible' to decrypt without knowledge of the key settings. This encryption method made the Enigma machine one of the most sophisticated cryptographic devices of its time and played a significant role in secure communication during World War II.
ufff.

# Encryption Mechanism

Firat of all enigma is a simple electrical circuit.
when we press a key, Electricity flows though it to the light bulb

so lets say press a key, current goes to the plugboard, 
there are
6 connector wires, so 12 plugs need to be plugged 
there are 26 places to plug one end of a wire then 25 for second end
then 24 for one end of second wire and 24 for second end and so on ......
which comes down to 

$$ {26! \over 6! * 10! * 2^{10} } = 150738274937250 $$

different arrangemets.
then current goes through rotors,
Enigma machine has 3 rotors and 5 rotors to choose from 
so 5x4x3 = 60 diffrent arrangements to choose the rotors
and then each rotor can have certain initial rotaion
which can be 26 so for 3 of them 26x26x26
Therefore we have 1054560 settings of rotors 

the plug board connections are applied during input as well as output
thus there is total of 158962555217826360000

** when you could use 10 plug wires, in original version there were 6 plugboard wires **

Then the character coorsponding to it will light up






