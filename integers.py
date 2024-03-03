#BDD
#Calculate the total number of bricks in array in A
#Check if its possible to distribute these  bricks evenly across all boxes
#If its possible we return the minimum number of mo ves needed to achieve
#If its not possible return -1

def solution(A):
    #Calculate the total number of bricks in the array
    total_bricks = sum(A)
    #checks if its possible to distribute the array evenly
    if total_bricks % len(A) != 0:
     return -1
    #calculate the target number of bricks in each box
    target_bricks = total_bricks // len(A)
    #initializes the moves count to 0
    moves = 0
    #iterates through the boxes and calculate the moves needed to reach the target
    for bricks in A:
        if bricks < target_bricks:
            #add the moves to the difference
            moves += target_bricks - bricks
    return moves
#calls the function
print(solution([5,10,15]))
print(solution([7,14,10]))

