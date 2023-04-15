import os

cur_dir = os.path.dirname(__file__)
os.chdir(cur_dir)

check_file = 'n'
while check_file != 'y':
    file = input("name of the file to edit (should have extension .mscx, and make sure the correct key signature is set in the score): ")
    check_file = input(f"is {file} the file? (y/n): ")
    

# error catching
key_dict = {'1':'C maj / A min','2':'G maj / E min','3':'D maj / B min',
            '4':'A maj / F# min','5':'E maj / C# min','6':'B maj / G# min',
            '7':'F# maj / D# min','8':'C# maj / A# min','9':'F maj / D min',
            '10':'Bb maj / G min','11':'Eb maj / C min','12':'Ab maj / F min',
            '13':'Db maj / Bb min','14':'Gb maj / Eb min','15':'Cb maj / Ab min'}
check_key = 'n'
while check_key != 'y':
    try:
        key = input("""select key signature (enter a number):
                    1. C maj / A min
                    2. G maj / E min
                    3. D maj / B min
                    4. A maj / F# min
                    5. E maj / C# min
                    6. B maj / G# min
                    7. F# maj / D# min
                    8. C# maj / A# min
                    9. F maj / D min
                    10. Bb maj / G min
                    11. Eb maj / C min
                    12. Ab maj / F min
                    13. Db maj / Bb min
                    14. Gb maj / Eb min
                    15. Cb maj / Ab min
                    """)
        check_key = input(f"is {key_dict[key]} the key signature? (y/n): ")
    except KeyError:
        print('\nplease enter a valid number for key signature\n')

### check the key signature is set in the file

with open(file, mode = "r") as f:
    # score = f.read()
    score = f.readlines()

# print(score)
# set keysig accidental if not c maj/a min -- user has done it, just take the input
# find notes that are in this key (by pitch), check if they are properly written (by tpc), replace with correct tpc if not

note_pitch_dict = {} # https://musescore.github.io/MuseScore_PluginAPI_Docs/plugins/html/pitch.html
for n in range(12): # note: 0 is C, 1 is C#, ..., 11 is B
    p = n # starting pitch
    p_li = [p]
    while p <= 127-12:
        p = p+12
        p_li.append(p)
    note_pitch_dict[n] = p_li

# print(note_pitch_dict)

key_pitch_dict = {} #'1':note_pitch_dict[0]}

k1_pitches = [] # C maj / A min pitches
k1_pitches.extend(note_pitch_dict[0])
k1_pitches.extend(note_pitch_dict[2])
k1_pitches.extend(note_pitch_dict[4])
k1_pitches.extend(note_pitch_dict[5])
k1_pitches.extend(note_pitch_dict[7])
k1_pitches.extend(note_pitch_dict[9])
k1_pitches.extend(note_pitch_dict[11])

k2_pitches = [] # G maj / E min pitches
k2_pitches.extend(note_pitch_dict[7])
k2_pitches.extend(note_pitch_dict[9])
k2_pitches.extend(note_pitch_dict[11])
k2_pitches.extend(note_pitch_dict[0])
k2_pitches.extend(note_pitch_dict[2])
k2_pitches.extend(note_pitch_dict[4])
k2_pitches.extend(note_pitch_dict[6])

k3_pitches = [] # D maj / B min pitches
k3_pitches.extend(note_pitch_dict[2])
k3_pitches.extend(note_pitch_dict[4])
k3_pitches.extend(note_pitch_dict[6])
k3_pitches.extend(note_pitch_dict[7])
k3_pitches.extend(note_pitch_dict[9])
k3_pitches.extend(note_pitch_dict[11])
k3_pitches.extend(note_pitch_dict[1])

k4_pitches = [] # A maj / F#m min pitches
k4_pitches.extend(note_pitch_dict[9])
k4_pitches.extend(note_pitch_dict[11])
k4_pitches.extend(note_pitch_dict[1])
k4_pitches.extend(note_pitch_dict[2])
k4_pitches.extend(note_pitch_dict[4])
k4_pitches.extend(note_pitch_dict[6])
k4_pitches.extend(note_pitch_dict[8])

k5_pitches = [] # E maj / C#m min pitches
k5_pitches.extend(note_pitch_dict[4])
k5_pitches.extend(note_pitch_dict[6])
k5_pitches.extend(note_pitch_dict[8])
k5_pitches.extend(note_pitch_dict[9])
k5_pitches.extend(note_pitch_dict[11])
k5_pitches.extend(note_pitch_dict[1])
k5_pitches.extend(note_pitch_dict[3])

k6_pitches = [] # B maj / G#m min pitches
k6_pitches.extend(note_pitch_dict[11])
k6_pitches.extend(note_pitch_dict[1])
k6_pitches.extend(note_pitch_dict[3])
k6_pitches.extend(note_pitch_dict[4])
k6_pitches.extend(note_pitch_dict[6])
k6_pitches.extend(note_pitch_dict[8])
k6_pitches.extend(note_pitch_dict[10])

k7_pitches = [] # F# maj / D#m min pitches
k7_pitches.extend(note_pitch_dict[6])
k7_pitches.extend(note_pitch_dict[8])
k7_pitches.extend(note_pitch_dict[10])
k7_pitches.extend(note_pitch_dict[11])
k7_pitches.extend(note_pitch_dict[1])
k7_pitches.extend(note_pitch_dict[3])
k7_pitches.extend(note_pitch_dict[5])

k8_pitches = [] # C# maj / A# min
k8_pitches.extend(note_pitch_dict[1])
k8_pitches.extend(note_pitch_dict[3])
k8_pitches.extend(note_pitch_dict[5])
k8_pitches.extend(note_pitch_dict[6])
k8_pitches.extend(note_pitch_dict[8])
k8_pitches.extend(note_pitch_dict[10])
k8_pitches.extend(note_pitch_dict[0])

k9_pitches = [] # F maj / D min
k9_pitches.extend(note_pitch_dict[5])
k9_pitches.extend(note_pitch_dict[7])
k9_pitches.extend(note_pitch_dict[9])
k9_pitches.extend(note_pitch_dict[10])
k9_pitches.extend(note_pitch_dict[0])
k9_pitches.extend(note_pitch_dict[2])
k9_pitches.extend(note_pitch_dict[4])

k10_pitches = [] # Bb maj / G min
k10_pitches.extend(note_pitch_dict[10])
k10_pitches.extend(note_pitch_dict[0])
k10_pitches.extend(note_pitch_dict[2])
k10_pitches.extend(note_pitch_dict[3])
k10_pitches.extend(note_pitch_dict[5])
k10_pitches.extend(note_pitch_dict[7])
k10_pitches.extend(note_pitch_dict[9])

k11_pitches = [] # Eb maj / C min
k11_pitches.extend(note_pitch_dict[3])
k11_pitches.extend(note_pitch_dict[5])
k11_pitches.extend(note_pitch_dict[7])
k11_pitches.extend(note_pitch_dict[8])
k11_pitches.extend(note_pitch_dict[10])
k11_pitches.extend(note_pitch_dict[0])
k11_pitches.extend(note_pitch_dict[2])

k12_pitches = [] # Ab maj / F min
k12_pitches.extend(note_pitch_dict[8])
k12_pitches.extend(note_pitch_dict[10])
k12_pitches.extend(note_pitch_dict[0])
k12_pitches.extend(note_pitch_dict[1])
k12_pitches.extend(note_pitch_dict[3])
k12_pitches.extend(note_pitch_dict[5])
k12_pitches.extend(note_pitch_dict[7])

k13_pitches = k8_pitches # Db maj / Bb min

k14_pitches = k7_pitches # Gb maj / Eb min

k15_pitches = k6_pitches # Cb maj / Ab min

key_pitch_dict = {'1':k1_pitches, '2':k2_pitches, '3':k3_pitches, 
                  '4':k4_pitches, '5':k5_pitches, '6':k6_pitches,
                  '7':k7_pitches, '8':k8_pitches, '9':k9_pitches,
                  '10':k10_pitches, '11':k11_pitches, '12':k12_pitches,
                  '13':k13_pitches, '14':k14_pitches, '15':k15_pitches}

# print(key_pitch_dict)

key_note_tpc_dict = {'1':{0:14,2:16,4:18,5:13,7:15,9:17,11:19}, # C maj / A min
                     '2':{7:15,9:17,11:19,0:14,2:16,4:18,6:20}, # G maj / E min
                     '3':{2:16,4:18,6:20,7:15,9:17,11:19,1:21}, # D maj / B min
                     '4':{9:17,11:19,1:21,2:16,4:18,6:20,8:22}, # A maj / F# min
                     '5':{4:18,6:20,8:22,9:17,11:19,1:21,3:23}, # E maj / C# min
                     '6':{11:19,1:21,3:23,4:18,6:20,8:22,10:24}, # B maj / G# min
                     '7':{6:20,8:22,10:24,11:19,1:21,3:23,5:25}, # F# maj / D# min
                     '8':{1:21,3:23,5:25,6:20,8:22,10:24,0:26}, # C# maj / A# min
                     '9':{5:13,7:15,9:17,10:12,0:14,2:16,4:18}, # F maj / D min
                     '10':{10:12,0:14,2:16,3:11,5:18,7:15,9:17}, # Bb maj / G min
                     '11':{3:11,5:13,7:15,8:10,10:12,0:14,2:16}, # Eb maj / C min
                     '12':{8:10,10:12,0:14,1:9,3:11,5:13,7:15}, # Ab maj / F min
                     '13':{1:9,3:11,5:13,6:8,8:10,10:12,0:14}, # Db maj / Bb min
                     '14':{6:8,8:10,10:12,11:7,1:9,3:11,5:13}, # Gb maj / Eb min
                     '15':{11:7,1:9,3:11,4:6,6:8,8:10,10:12} # Cb maj / Ab min
                    }

# check score for pitches in the key, if there are accidentals / tpc is not right, fix
# pitches that are in the key and have accidentals might need fix (check what happens when the accidental is natural and you need it after changing a note)

pitch = -1 # not yet assigned
check_tpc = 0 # 0 is default, 1 means check tpc
score_updated = ''
n = 1

for line in score:
    # print(f'line {n}',line)
    # print('line:',line)
    if '<pitch' in line: # and line.split('</pitch>')[0].split('<pitch>')[1]:
        # print('pitch line:')
        pitch = int(line.split('</pitch>')[0].split('<pitch>')[1])
        # print('pitch:',pitch)
        if pitch in key_pitch_dict[key]: # pitch is in key, check tpc
            check_tpc = 1
        # print('check_tpc:',check_tpc)
        score_updated += line
    
    elif '<tpc' in line and check_tpc == 1:
        # ..
        # get note from pitch, and get correct tpc 
        # print('tpc line and check_tpc:')
        note = pitch%12
        # print('note:',note)
        correct_tpc = key_note_tpc_dict[key][note]
        # print('correct_tpc:',correct_tpc)
        tpc = int(line.split('</tpc>')[0].split('<tpc>')[1])
        # print('tpc:',tpc)
        if tpc != correct_tpc:
            # print('tpc != correct_tpc')
            line_updated = line.split(str(tpc))[0]+str(correct_tpc)+line.split(str(tpc))[1]
            # print('line_updated:',line_updated)
            score_updated += line_updated
            # update line
        else:
            score_updated += line
        check_tpc = 0 # restore default

    else: # just append to score_updated
        score_updated += line #+'\n'
    
    n+=1
        

# print(score_updated)

with open(f"{file.split('.mscx')[0]}_.mscx", mode = "w") as f:
    score = f.write(score_updated)
    
