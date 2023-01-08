def parce_int(integer):
    str_list = []
    string = str(integer)
    int_ones = {'one':'1','two':'2','three':'3','four':'4','five':'5',
                    'six':'6','seven':'7','eight':'8','nine':'9','ten':'10'}
    int_teens = {'eleven':'11','twelve':'12','thirteen':'13','fourteen':'14',
                    'fifteen':'15','sixteen':'16','seventeen':'17','eighteen':'18',
                    'nineteen':'19'}
    int_tens = {'twenty':'2','thirty':'3','fourty':'4','fifty':'5',
                    'sixty':'6','seventy':'7','eighty':'8','ninety':'9'}
    #----------------------------------------------------------------------------------------- 
    if string == '0':
        return print ('zero')

    if len(string) == 1:
        for key,value in int_ones.items():
            if string == value:
                str_list.append(key)
                int_str = ''.join(str_list)
    
    if len(string) == 2:
        if string[0] == '1':
            for key,value in int_teens.items():
                if string == value:
                    str_list.append(key)
            int_str = ''.join(str_list)
        if string[0] != '1':
            for key,value in int_tens.items():
                if string[0] == value:
                    str_list.append(key)
                    for key,value in int_ones.items():
                        if string[1] == value:
                            str_list.append(key)

            int_str = '-'.join(str_list)

    if len(string) == 3:
        for keys,values in int_ones.items():
            if string[0] == values:
                str_list.append(keys)
                str_list.append('houndred')

                if string [1] == '1':
                    for key,value in int_teens.items():
                        new_str = string[1] + string[2]
                        if new_str == value:
                            str_list.append(key)
                    int_str = ' '.join(str_list)

                if string[1] != '1':
                    for keys,values in int_tens.items():
                        if string[1] == values:
                            str_list.append(keys)
                            for keys,values in int_ones.items():
                                if string[2] == values:
                                    str_list.append(keys)

                    int_str = ' '.join(str_list)                

    if len(string) == 4:
        for keys,values in int_ones.items():
            if string[0] == values:
                str_list.append(keys)
                str_list.append('thousand')
                new_str = string[1] + string[2] + string[3]

                if len(new_str) == 3:
                    for keys,values in int_ones.items():
                        if new_str[0] == values:
                            str_list.append(keys)
                            str_list.append('houndred')

                            if new_str [1] == '1':
                                for key,value in int_teens.items():
                                    new_str = new_str[1] + new_str[2]
                                    if new_str == value:
                                        str_list.append(key)

                            if new_str[1] != '1':
                                for keys,values in int_tens.items():
                                    if new_str[1] == values:
                                        str_list.append(keys)
                                        for keys,values in int_ones.items():
                                            if new_str[2] == values:
                                                str_list.append(keys)

        int_str = ' '.join(str_list)
    
    if len(string) == 5:
        if string[0] == '1':
            for keys,values in int_teens.items():
                if (string[0] + string[1]) == values:
                    str_list.append(keys)
                    str_list.append('thousand')

            for keys,values in int_ones.items():
                if string[2] == values:
                    str_list.append(keys)
                    str_list.append('houndred')
            
            if string[3] == '1':
                for keys,values in int_teens.items():
                    if (string[3] + string[4]) == values:
                        str_list.append(keys)
            if string[3] != '1':
                for keys,values in int_tens.items():
                    if string[3] == values:
                        str_list.append(keys)
                        for keys,values in int_ones.items():
                            if string[4] == values:
                                str_list.append(keys)

        if string[0] != '1':
            for keys,values in int_tens.items():
                if string[0] == values:
                    str_list.append(keys)
                    
            for keys,values in int_ones.items():
                if string[1] == values:
                    str_list.append(keys)
            str_list.append('thousand')

            for keys,values in int_ones.items():
                if string[2] == values:
                    str_list.append(keys)
                    str_list.append('houndred')
            
            if string[3] == '1':
                for keys,values in int_teens.items():
                    if (string[3] + string[4]) == values:
                        str_list.append(keys)
            if string[3] != '1':
                for keys,values in int_tens.items():
                    if string[3] == values:
                        str_list.append(keys)
                        for keys,values in int_ones.items():
                            if string[4] == values:
                                str_list.append(keys)
        
        int_str = ' '.join(str_list)
    
    if len(string) == 6:
        for keys,values in int_ones.items():
            if string[0] == values:
                str_list.append(keys)
                str_list.append('houndred')

        if string[1] == '1':
            for keys,values in int_teens.items():
                if (string[0] + string[1]) == values:
                    str_list.append(keys)
                    str_list.append('thousand')
            for keys,values in int_ones.items():
                if string[3] == values:
                    str_list.append(keys)
                    str_list.append('houndred')
            
            if string[4] == '1':
                for keys,values in int_teens.items():
                    if (string[3] + string[4]) == values:
                        str_list.append(keys)
            if string[4] != '1':
                for keys,values in int_tens.items():
                    if string[4] == values:
                        str_list.append(keys)
                        for keys,values in int_ones.items():
                            if string[5] == values:
                                str_list.append(keys)

        if string[1] != '1':
            for keys,values in int_tens.items():
                if string[1] == values:
                    str_list.append(keys)
                    
            for keys,values in int_ones.items():
                if string[2] == values:
                    str_list.append(keys)
            str_list.append('thousand')

            for keys,values in int_ones.items():
                if string[3] == values:
                    str_list.append(keys)
                    str_list.append('houndred')
            
            if string[4] == '1':
                for keys,values in int_teens.items():
                    if (string[3] + string[4]) == values:
                        str_list.append(keys)
            if string[4] != '1':
                for keys,values in int_tens.items():
                    if string[4] == values:
                        str_list.append(keys)
                        for keys,values in int_ones.items():
                            if string[5] == values:
                                str_list.append(keys)
        
        int_str = ' '.join(str_list)
    
    if len(string) == 7:
        return print ('one million')

    return print (integer,':',int_str)

parce_int(0)
parce_int(1)
parce_int(11)
parce_int(47)
parce_int(101) #error
parce_int(111)
parce_int(150)
parce_int(171) 
parce_int(764)
parce_int(1001) #error
parce_int(1011) #error
parce_int(1028) #error
parce_int(2354)
parce_int(10001)
parce_int(12348)
parce_int(54711)
parce_int(78428)
parce_int(100001) #error
parce_int(111999)

#this file is edited
