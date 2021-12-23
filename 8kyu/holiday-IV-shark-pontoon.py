def shark(pontoon_distance, shark_distance, you_speed, shark_speed, dolphin):
    if dolphin == True:
        shark_speed = shark_speed /2
    if shark_distance == 0:
        return "Shark Bait!"
    return "Alive!" if you_speed/pontoon_distance >= shark_speed/shark_distance else "Shark Bait!"
