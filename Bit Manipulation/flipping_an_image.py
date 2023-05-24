'''

PROBLEM: 

Given that an image is represented by an (nxn) matrix containing 0s and 1s, 
flip and invert the image, and return the resultant image. 

Horizontally flipping an image means that the mirror image of the matrix 
should be returned. Flipping [1,0,0] horizontally results in [0,0,1] . 

Inverting an image means that every 0 is replaced by 1 , and every 1 is 
replaced by 0 . Inverting [0,1,1] results in [1,0,0] .

---------------------------
PATTERN: BIT MANIPULATION
---------------------------

'''





def flip_and_invert_image(image):
    
    
    row_len = len(image)
    col_len = len(image[0])

    

    for i in range(row_len) :
        row = image[i]

        xor = 1
        left, right = 0, col_len - 1

        while left < right :
            row[left], row[right] = row[right], row[left]

            row[left] = row[left] ^ xor
            row[right] = row[right] ^ xor

            left += 1
            right -= 1
        
        if left == right :
            row[left] = row[left] ^ xor
    

    return image





