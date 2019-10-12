import csv 
with open('assest.csv','a',newline = '') as csvfile:
    writer = csv.writer(csvfile,dialect='excel')
    header=['小區名稱','地址','建築年份','樓棟','單元','戶室','朝向','面積']
    writer.writerow(header)
title = input('請輸入小區名稱:')
address = input('請輸入小區地址:')
year = input('請輸入小區建造年份:')
block = input('請輸入樓棟:')
unit = input('請輸入單元號:')

unit_loop = True
while unit_loop:
    unit = input('請輸入單元號:')
    strat_floor = input('請輸入始樓層:')
    end_floor = input('請輸入結束樓層:')
    
    input('接下來請輸入起始層房間的門牌號、朝向及面積，按任意鍵繼續')

    strat_floor_rooms = {}
    floor_last_number = []
    
    room_loop = True
    while room_loop:
        last_number = input('請輸入起始樓層戶室的尾號(如01、02)：')
        floor_last_number.append(last_number)
        room_number = int(strat_floor+last_number)
        direction = input('請輸入%d的朝向，南北朝向輸入1，東西朝向輸入2：' % room_number)
        area = input('請輸入%d的面積' % room_number)

        strat_floor_rooms[room_number] = [diretion,area]
        continued = input('是否需要輸入下個尾號？按 n 結束，按任意鍵繼續：')
        
        if continued == 'n':
            room_loop = False
        else:
            room_loop = True
    unit_rooms = {}
    unit_rooms[strat_floor] = strat_floor_rooms
    for floor in range(int(strat_floor)+1,int(end_floor)+1):
        
        floor_rooms = {}
        for i in range(len(strat_floor_rooms)):
            number = str(floor)+floor_last_number[i]
            info = strat_floor_rooms[int(strat_floor+floor_last_number[i])]
            floor_room[number] = info
        unit_rooms[floor] = floor_rooms
    unit_continue = input('是否輸入下一個單元，按 n 退出，按任意鍵繼續')

    with open ('assest.csv','a',newline='')as csvfile:
        writer = csv.writer(csvfile,dialect='excel')
        for sub_dict in unit_rooms.values():
            for room,info in sub_dict:
                dire = ['','南北','東西']
                writer.writerow([title,address,year,block,unit,room,dire[info[0]],info[1]])
    if unit_continue == 'n':
        unit_loop = False
    else:
        unit_loop = True
print('運行通過！')
        
