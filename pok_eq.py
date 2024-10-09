import math
def Hidden_power_type(stat_arr):
    binary_arr = [None] * 6
    type_arr = ["Fighting","Flying","Poision","Ground","Rock","Bug","Ghost","Steel","Fire","Water","Grass","Electric","Psychic","Ice","Dragon","Dark"]
    for i in range(len(stat_arr)):
        if stat_arr[i]%2 == 0:
            binary_arr[i] = 0
        else:
            binary_arr[i] = 1
    Spd = binary_arr[5]
    sAtk = binary_arr[3]
    sDef = binary_arr[4]
    binary_arr[3] = Spd
    binary_arr[4] = sAtk
    binary_arr[5] = sDef
    type_value = 0
    for j in range(len(binary_arr)):
        type_value += (binary_arr[j]) * pow(2,j)
    type_value = math.floor((type_value*15)/63)
    return type_value


def Hidden_power_damage(stat_arr):
    binary_arr = [None] * 6
    for i in range(len(stat_arr)):
        temp = bin(stat_arr[i])
        if temp[len(temp)-2:len(temp)-1] == 'b':
            binary_arr[i] = 0
        else:
            binary_arr[i] = int(temp[len(temp)-2:len(temp)-1])
    Spd = binary_arr[5]
    sAtk = binary_arr[3]
    sDef = binary_arr[4]
    binary_arr[3] = Spd
    binary_arr[4] = sAtk
    binary_arr[5] = sDef
    damage_value = 0
    for j in range(len(stat_arr)):
        damage_value += (binary_arr[j]) * pow(2,j)
    damage_value = math.floor((damage_value*40/63) + 30)
    return damage_value

def array_total_2d(array,index):
    total = 0
    for i in range(len(array)):
        total += array[i][index]
    return total


def Possible_HP(stat_arr):
    possible_types = [[0 for i in range(0,2)] for j in range(0,16)]
    possible_stats = [2,3,6,7,10,11,14,15,18,19,22,23,26,27,30,31]
    set_stats = []
    damage_check = 0
    for i in range(len(stat_arr)):
        if stat_arr[i] == 0:
            set_stats.append(i)
        else:
            temp = bin(stat_arr[i])
            if temp[len(temp)-2:len(temp)-1] == '1':
                damage_check += 1
    for i in range(0,16):
        stat_arr[set_stats[0]] = possible_stats[i]
        for j in range(0,16):
            stat_arr[set_stats[1]] = possible_stats[j]
            for k in range(0,16):
                stat_arr[set_stats[2]] = possible_stats[k]
                type_value = Hidden_power_type(stat_arr)  
                possible_types[type_value][0] += 1
                if damage_check == 3:
                    if Hidden_power_damage(stat_arr) == 70:
                        possible_types[type_value][1] += 1
                        #possible_types[type_value].append(stat_arr)
    return possible_types



def stat_generator(grouped_stats):
    pointers = [[0,0],[1,0],[2,0]]
    type_dist = [[0 for i in range(0,2)] for j in range(0,16)]
    temp_array = []
    while True:
        stat_set = [0,0,0,0,0,0]
        stat_set[pointers[0][0]] = grouped_stats[pointers[0][0]][pointers[0][1]]
        stat_set[pointers[1][0]] = grouped_stats[pointers[1][0]][pointers[1][1]]
        stat_set[pointers[2][0]] = grouped_stats[pointers[2][0]][pointers[2][1]]

        temp_array = Possible_HP(stat_set)
        for i in range(0,16):
            for j in range(0,2):
                type_dist[i][j] += temp_array[i][j]

        #increment pointer 3
        if pointers[2][1] == 0:
            pointers[2][1] = 1
        else:
            pointers[2][0] += 1
            pointers[2][1] = 0
        
        if  pointers[2][0] == 6:#if pointer 3 cycle complete, increment pointer 2
            if pointers[1][1] == 0:
                pointers[1][1] = 1
            else:#set pointer 2 to next stat
                pointers[1][0] += 1
                pointers[1][1] = 0
            pointers[2][1] = 0#sets pointer 3 ahead of 2
            pointers[2][0] = pointers[1][0] + 1

        if pointers[1][0] == 5:#if pointer 2 cycle complete, increment pointer 1
            if pointers[0][1] == 0:
                pointers[0][1] = 1
            else:
                pointers[0][0] += 1
                pointers[0][1] = 0
            #reset pointers 2 & 3
            pointers[1][0] = pointers[0][0] + 1
            pointers[2][0] = pointers[1][0] + 1
            pointers[1][1] = 0
            pointers[2][1] = 0

        if pointers[0][0] == 4:
            break
        
            
    return type_dist
    
def HP_from_parents(parent1,parent2):
    type_arr = ["Fighting","Flying","Poision","Ground","Rock","Bug","Ghost","Steel","Fire","Water","Grass","Electric","Psychic","Ice","Dragon","Dark"]
    spacing = ("          ")
    grouped_stats = [[0 for i in range(0,2)] for j in range(0,6)]
    for i in range(0,6):
        grouped_stats[i][0] = parent1[i]
        grouped_stats[i][1] = parent2[i]
    data_set = stat_generator(grouped_stats)
    total = array_total_2d(data_set,0)
    for i in range(0,16):
        if data_set[i][0] != 0:
            string = type_arr[i] + spacing[len(type_arr[i]):]
            #print(string,": ",data_set[i][0] / total,": ",data_set[i][1] / total)
    return data_set

    
def menu():
    print("----------------------------------------")
    print("Welcome to PBP")
    print("______________")
    print("Please input parent data")

    
def main():
    P1_stats = [0,31,31,0,22,0]
    P2_stats = [0,31,31,0,22,0]
    stat_names = ["HP","ATK","DEF","SATK","SDEF","SPD"]
    spacing = "    "
    menu()
    print("Father: ")
    for i in range(0,6):
        string = stat_names[i] + spacing[len(stat_names[i]):] + ": "
        P1_stats[i] = int(input(string))
    print("Mother: ")
    for i in range(0,6):
        string = stat_names[i] + spacing[len(stat_names[i]):] + ": "
        P2_stats[i] = int(input(string))
    print("-------------------------")
    print("|   TYPE   |  TYPE PROB  |  MAX DAMAGE PROB  |")
    HP_from_parents(P1_stats,P2_stats)    


