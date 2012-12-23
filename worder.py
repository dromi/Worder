import random
import time

rounds = 5
spr = 3
r = random
t = time

"Start by loading in phrases"

inp = open('phrases.txt')
outp = open('res.txt', 'r+')

phrases_raw = inp.read();

phrase_list = []

while (phrases_raw != ''):
    p = phrases_raw.partition('\r\n')
    phrase_list.append(p[0])
    phrases_raw = p[2]

"Execute the main test"

print("""
Welcome to worder!
Please type in the sentences that appead as quick as possible. Press Enter to finish a sentence and move on.
There will be 5 rounds in total, each requiring 7 sentences to be typed.
""")

wordr = 0
timer = 0
wpmr = 0


for i in xrange(rounds):

    phrases = list(phrase_list)
    wordt = 0
    timet = 0
    wpmt = 0
    
    raw_input('Press Enter to start next round')

    outp.write('-------------------------ROUND ' + str(i) + '-------------------------\n')

    "Start throwing sentences at user"    
    for j in xrange(spr):

        num = round(r.random()*len(phrases)-1)
        sentence = phrases.pop(int(num))
        print ""

        print "Please enter --> " + sentence
        
        print ""
        start = t.time()
        user_sentence = raw_input('-->')
        stop = t.time()
        print ""

        words = sentence.count(' ') + 1
        timed = stop-start
        outp.write('\nSENTENCE NO: ' + str(j) + '\n')
        outp.write('COMP:   ' + sentence +'\n')
        outp.write('USER:   ' + user_sentence +'\n')
        outp.write('Time: ' + str(timed) + ' Words: ' + str(words) + ' WPM: ' + str( (60 / (timed)) * words ) + '\n')
        timet += timed
        wordt += words
        wpmt += ( (60 / (timed)) * words )

    outp.write('-------------------------END OF ROUND-------------------------\n')
    outp.write('\nROUND RESULTS: \n')
    
    outp.write('Time: ' + str(timet) + ' Words: ' + str(wordt) + ' WPM: ' + str( wpmt/spr ) + '\n')

    print("End of round " + str(i))

    timer += timet
    wordr += wordt
    wpmr += (wpmt/spr)
    

print("""The program has finished. Thank you for your time!""")

outp.write('*************************END OF TEST************************\n')
outp.write('\nFINAL RESULTS: \n')
outp.write('Time: ' + str(timer) + ' Words: ' + str(wordr) + ' WPM: ' + str( wpmr/rounds ) + '\n')

outp.write('**********************************************************************')


outp.close()
