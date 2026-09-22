def count_smileys(arr):
    valid_eyes = [':', ';']
    valid_nose = ['-','~']
    valid_mouth = ['D', ')']
    count = 0
    for x in arr:
        if len(x)==3:
            eyes, nose, mouth = x
            if eyes in valid_eyes and nose in valid_nose and mouth in valid_mouth:
                count += 1
        elif len(x)==2:
            eyes, mouth = x
            if eyes in valid_eyes and mouth in valid_mouth:
                count += 1
    return count