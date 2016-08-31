#バブルソートをするプログラム

# -*- coding: utf-8 -*-

list = [1,14,51,4,1,9,19,8,10,8,9,3]

#バブルソートの処理をする関数
def bubble_sort(list):

    for i in range(0, len(list)):
        for j in reversed(range(len(list))):
            if(j == i):
                break
            if(list[j-1] > list[j]):
                tmp = list[j]
                list[j] = list[j-1]
                list[j-1] = tmp
#                print(list)                
    return list

if __name__ == "__main__":

    print("ソート前：", list)
    bubble_sort(list)
    print("ソート後：", list)
