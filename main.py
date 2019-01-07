import math
import cv2
import numpy as np

def PatternChecker(number, gridCount):

    gridHeight = int(math.sqrt(gridCount))

    _tempNumber = number
    blockSize = 8
    img = np.zeros((gridHeight * blockSize + blockSize * 2, gridHeight * blockSize, 3), np.uint8)
    #(cv2.cvCreateImage(cv2.cvSize(gridHeight * blockSize, gridHeight * blockSize + blockSize * 2), 8, 3)

    thickness = 1
    lineType = 8
    start = tuple((0, 0))

    end = (gridHeight * blockSize,gridHeight * blockSize + blockSize * 2)
    color = (255, 255, 255)
    cv2.rectangle(img, start, end, (255, 255, 255), thickness, lineType)

    for i in range(0, gridCount):
        x = _tempNumber & 0x01;
        _tempNumber = _tempNumber >> 1
        cellCount = i%gridHeight
        rowCount = int(i / gridHeight)
        if x == 1:
            cv2.line(img, ((cellCount)* blockSize, rowCount * blockSize + blockSize), (((cellCount)+1) * blockSize, rowCount * blockSize + blockSize * 2), (255, 255, 255), 2, 8)
        else:
            cv2.line(img, ((cellCount)* blockSize, rowCount * blockSize + blockSize * 2), (((cellCount)+1) * blockSize, rowCount * blockSize + blockSize), (255, 255, 255), 2, 8)

    h, w = img.shape[:2]
    mask = np.zeros((h + 2, w + 2), np.uint8)
    cv2.floodFill(img, mask, (int(blockSize / 2), int(blockSize / 2)), (120, 200, 50))

    s = img[int(gridHeight * blockSize + blockSize + blockSize / 2), int(gridHeight * blockSize / 2)]

    '''
    cv2.imshow('test', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
    '''
    filename = "image" + str(number) + ".jpg"
    success = False
    if s[2] > 0:
        filename = "results/success/image" + str(number) + ".jpg"
        success = True;
    else:
        filename = "results/failed/image" + str(number) + ".jpg"

    '''
    cv2.imwrite(filename, img)
    '''
    return success


def main():
    count = 0
    n = 3 # n x n grid size
    max = int(math.pow(2,n*n))

    for i in range(0, max):
        x = PatternChecker(i, n*n)
        if x == True:
            count += 1

    print('Count: ', count)

if __name__ == '__main__':
    main()