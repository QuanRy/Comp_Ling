import re
import os
import sqlite3
import random
from tomita.tonality import func_tonality


def tomita(text_write, id, datePost):
    con = sqlite3.connect("sema.db")
    
    text_file = open("/home/student/sema/tomita/input.txt", "w")
    text_file.write(text_write)
    text_file.close()
    
    os.system("cd tomita/; ./tomita-parser config.proto")

    text = open('/home/student/sema/tomita/output.txt', 'r', encoding='utf-8')
    text = text.read()

    print(text)

    sur = re.finditer("Name = ", text)
    startSur = []
    endSur = []

    texts = re.finditer("Text = ", text)
    startText = []
    endText = []

    quate = re.finditer("}", text)
    startQuate = []


    for item in sur:
        startSur.append(item.regs[0][0])
        endSur.append(item.regs[0][1])
    for item in texts:
        startText.append(item.regs[0][0])
        endText.append(item.regs[0][1])
    for item in quate:
        startQuate.append(item.regs[0][0])

    print(len(startSur))
    
    if len(startSur) == 0:
        try:
            with sqlite3.connect("sema.db") as con:
                cur = con.cursor()
                state = 'not done'
                cur.execute("INSERT into props(id_props, facts, text, tonality, dates, id_post) values (?, ?, ?, ?, ?, ?)", (cur.lastrowid, str("-"), str("-"), str("-"), str(datePost), int(id)))
                con.commit()
                state = 'done'
                msg = 'success'
        except:
            msg = 'not success'
    else:
        for i in range(len(startSur)):
            fact = (text[endSur[i] : startText[i]])
            partText = (text[endText[i] : startQuate[i]])        
            
            fact = fact.upper()
                
                
            res_tonal = func_tonality(partText)
            
            # ran = random.random()
            # if ran >= 0.1:
            #     res_tonal = "Positive"
            # else:
            #     res_tonal = "Negative"
            

            try:
                with sqlite3.connect("sema.db") as con:
                    cur = con.cursor()
                    state = 'not done'
                    cur.execute("INSERT into props(id_props, facts, text, tonality, dates, id_post) values (?, ?, ?, ?, ?, ?)", (cur.lastrowid, str(fact), str(partText), str(res_tonal), str(datePost), int(id)))
                    con.commit()
                    state = 'done'
                    msg = 'success'
            except:
                msg = 'not success'
            print (str(state))
    print("finally")
    	