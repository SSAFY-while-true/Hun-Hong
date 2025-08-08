if __name__ == "__main__":
    H, W = map(int, input().split())

    heights = list(map(int, input().split()))

    left_max = [0] * W
    right_max = [0] * W
    left_max[0] = heights[0]
    right_max[W-1] = heights[W-1]

    for i in range(1, W):
        if heights[i] > left_max[i-1]:
            left_max[i] = heights[i]
        else:
            left_max[i] = left_max[i-1]
        
        if heights[W-1-i] > right_max[W-i]:
            right_max[W-1-i] = heights[W-1-i]
        else:
            right_max[W-1-i] = right_max[W-i]
    
    water = 0
    for i in range(W):
        water += min(left_max[i], right_max[i]) - heights[i]
    
    print(water)