# Program that gets list of unsorted numbers, a sort method, 
# and a sort order (ascending or descending) from user and
# returns the list sorted as requested

# import pygame

def bubblesort(nlist, descending):

    if descending:
        end_pos = len(nlist)-1

        while end_pos > 1:
            for i in range(end_pos):
                if nlist[i] < nlist[i+1]:  # then swap them
                    nlist[i], nlist[i+1] = nlist[i+1], nlist[i]
                print(num_list, end_pos)
            end_pos -= 1
    else:
        end_pos = len(nlist)-1

        while end_pos > 1:
            for i in range(end_pos):
                if nlist[i] > nlist[i+1]:  # then swap them
                    nlist[i], nlist[i+1] = nlist[i+1], nlist[i]
                print(num_list, end_pos)
                
            end_pos -= 1
    

# num_list = [1, 222, 1000, 10, 0, 9, 7, 8, 1, 3, 6, 5, 2, 4]
# num_list = [1, 222, 1000, 10, 0]
num_list = []
while True:
    try:
        next_num = int(input("Enter an Integer or return to end list: "))
        num_list.append(next_num)
    except:
        break
sort_type = input("Ascending (A) or Descending (D)? ").lower()

print(num_list, sort_type)
bubblesort(num_list, sort_type=='d')
print(num_list)

# pygame.init()