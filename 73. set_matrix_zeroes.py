def setZeroes(arr):
    rows = len(arr)
    cols = len(arr[0])
    for i in range(rows):
        for j in range(cols):
            if arr[i][j]==0:
                ind = i-1
                while ind>=0:
                    if arr[ind][j] != 0:
                        arr[ind][j] = "a"
                    ind-=1
                ind = i+1
                while ind<rows:
                    if arr[ind][j] != 0:
                        arr[ind][j] = "a"
                    ind+=1
                ind = j-1
                while ind>=0:
                    if arr[i][ind] != 0:
                        arr[i][ind] = "a"
                    ind-=1
                ind = j+1
                while ind<cols:
                    if arr[i][ind] != 0:
                        arr[i][ind] = "a"
                    ind+=1

    for i in range(rows):
        for j in range(cols):
            if arr[i][j]=="a":
                arr[i][j]=0

    return arr