def countOdds(low,high):
    if low%2==0 and high%2==0:
        return (high-low)//2
    else:
        return (high-low)//2+1