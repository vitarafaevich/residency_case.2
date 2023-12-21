"""
Kotlyarova Polina 92
Rafaevich Vita 92
Leonov Kirill 89
"""

import ru_local as ru
import datetime
from datetime import date

d = datetime.datetime.today()
do = d.date()
d_before = (do - datetime.timedelta(days=365))
print(ru.PERIOD, d_before, ru.R_2, do, ru.PERIOD_)
prd = input()
if prd.lower() == ru.R_4 or prd.lower() == 'yes':
    print(ru.RESIDENT)
    a = input(ru.RES_Q_1)
    if a.lower() == ru.R_4 or a.lower() == 'yes':
        print(ru.ANSWER, "9%")
    else:
        b = input(ru.RES_Q_2)
        if b.lower() == ru.R_4 or b.lower() == 'yes':
            print(ru.ANSWER, "35%")
        else:
            c = input(ru.RES_Q_3)
            if c.lower() == ru.R_4 or c.lower() == 'yes':
                print(ru.ANSWER, "35%")
            else:
                d = input(ru.RES_Q_4)
                if d.lower() == ru.R_4 or d.lower() == 'yes':
                    print(ru.ANSWER, "35%")
                else:
                    e = input(ru.RES_Q_5)
                    if e.lower() == ru.R_4 or e.lower() == 'yes':
                        print(ru.ANSWER, "13%")
                    else:
                        f = input(ru.RES_Q_6)
                        if f.lower() == ru.R_4 or f.lower() == 'yes':
                            print(ru.ANSWER, "15% + 650 000", ru.CURRENCY)
                        else:
                            print(ru.ANSWER, "13%")
else:
    question2 = input(ru.PRD_EXIT)
    if question2.lower() == ru.R_NO or question2.lower() == 'no':
        print(ru.NON_RESIDENT)
        question2_1 = input(ru.NONRES_Q_1)
        question2_1 = question2_1.strip('.,!?-:;_ ')
        if question2_1.lower() == ru.R_4 or question2_1.lower() == 'yes':
            print(ru.ANSWER, '15%')
        else:
            question2_2 = input(ru.NONRES_Q_2)
            question2_2 = question2_2.strip('.,!?-:;_ ')
            if question2_2.lower() == ru.R_4 or question2_2.lower() == 'yes':
                print(ru.ANSWER, '15%')
            else:
                question2_3 = input(ru.NONRES_Q_3)
                question2_3 = question2_3.strip('.,!?-:;_ ')
                if question2_3.lower() == ru.R_4 or question2_3.lower() == 'yes':
                    print(ru.ANSWER, '5%')
                else:
                    question2_4 = input(ru.NONRES_Q_4)
                    question2_4 = question2_4.strip('.,!?-:;_ ')
                    if question2_4.lower() == ru.R_4 or question2_4.lower() == 'yes':
                        question2_5 = input(ru.NONRES_Q_5)
                        question2_5 = question2_5.strip('.,!?-:;_ ')
                        if question2_5.lower() == ru.R_4 or question2_5.lower() == 'yes':
                            print(ru.ANSWER, '15% + 650 000', ru.CURRENCY)
                        else:
                            print(ru.ANSWER, '13%')
                    else:
                        question2_6 = input(ru.NONRES_Q_6)
                        question2_6 = question2_6.strip('.,!?-:;_ ')
                        if question2_6.lower() == ru.R_4 or question2_6.lower() == 'yes':
                            question2_5 = input(ru.NONRES_Q_5)
                            question2_5 = question2_5.strip('.,!?-:;_ ')
                            if question2_5.lower() == ru.R_4 or question2_5.lower() == 'yes':
                                print(ru.ANSWER, '15% + 650 000', ru.CURRENCY)
                            else:
                                print(ru.ANSWER, '13%')
                        else:
                            print(ru.ANSWER, '30%')
    else:
        d = datetime.datetime.today()
        do = d.date()
        d_before = (do - datetime.timedelta(days=365))
        if question2.lower() == ru.R_4 or question2.lower() == 'yes':
            f = int(input(ru.R_5))
            total = 0
            for i in range(f):
                k = input(ru.R_6)
                b = input(ru.R_7)
                k = k.split('-')
                b = b.split('-')
                kk = datetime.date(int(k[0]), int(k[1]), int(k[2]))
                bb = datetime.date(int(b[0]), int(b[1]), int(b[2]))
                cc = bb - kk
                n = str(cc.days)
                total += int(n)
            print(total)
            if total <= 183:
                print(ru.R_8)
                a = input(ru.RES_Q_1)
                if a.lower() == ru.R_4 or a.lower() == 'yes':
                    print(ru.ANSWER, "9%")
                else:
                    b = input(ru.RES_Q_2)
                    if b.lower() == ru.R_4 or b.lower() == 'yes':
                        print(ru.ANSWER, "35%")
                    else:
                        c = input(ru.RES_Q_3)
                        if c.lower() == ru.R_4 or c.lower() == 'yes':
                            print(ru.ANSWER, "35%")
                        else:
                            d = input(ru.RES_Q_4)
                            if d.lower() == ru.R_4 or d.lower() == 'yes':
                                print(ru.ANSWER, "35%")
                            else:
                                e = input(ru.RES_Q_5)
                                if e.lower() == ru.R_4 or e.lower() == 'yes':
                                    print(ru.ANSWER, "13%")
                                else:
                                    f = input(ru.RES_Q_6)
                                    if f.lower() == ru.R_4 or f.lower() == 'yes':
                                        print(ru.ANSWER, "15% + 650 000", ru.CURRENCY)
                                    else:
                                        print(ru.ANSWER, "13%")
            else:
                print(ru.R_9)
                question2_1 = input(ru.NONRES_Q_1)
                question2_1 = question2_1.strip('.,!?-:;_ ')
                if question2_1.lower() == ru.R_4 or question2_1.lower() == 'yes':
                    print(ru.ANSWER, '15%')
                else:
                    question2_2 = input(ru.NONRES_Q_2)
                    question2_2 = question2_2.strip('.,!?-:;_ ')
                    if question2_2.lower() == ru.R_4 or question2_2.lower() == 'yes':
                        print(ru.ANSWER, '15%')
                    else:
                        question2_3 = input(ru.NONRES_Q_3)
                        question2_3 = question2_3.strip('.,!?-:;_ ')
                        if question2_3.lower() == ru.R_4 or question2_3.lower() == 'yes':
                            print(ru.ANSWER, '5%')
                        else:
                            question2_4 = input(ru.NONRES_Q_4)
                            question2_4 = question2_4.strip('.,!?-:;_ ')
                            if question2_4.lower() == ru.R_4 or question2_4.lower() == 'yes':
                                question2_5 = input(ru.NONRES_Q_5)
                                question2_5 = question2_5.strip('.,!?-:;_ ')
                                if question2_5.lower() == ru.R_4 or question2_5.lower() == 'yes':
                                    print(ru.ANSWER, '15% + 650 000', ru.CURRENCY)
                                else:
                                    print(ru.ANSWER, '13%')
                            else:
                                question2_6 = input(ru.NONRES_Q_6)
                                question2_6 = question2_6.strip('.,!?-:;_ ')
                                if question2_6.lower() == ru.R_4 or question2_6.lower() == 'yes':
                                    question2_5 = input(ru.NONRES_Q_5)
                                    question2_5 = question2_5.strip('.,!?-:;_ ')
                                    if question2_5.lower() == ru.R_4 or question2_5.lower() == 'yes':
                                        print(ru.ANSWER, '15% + 650 000', ru.CURRENCY)
                                    else:
                                        print(ru.ANSWER, '13%')
                                else:
                                    print(ru.ANSWER, '30%')
