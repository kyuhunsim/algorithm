paper=[]
N=int(input())
for i in range(N):
    paper.append(list(map(int,input().split())))

def count_colored_paper(n, paper):
    # Initialize counts for white and blue paper
    white = 0
    blue = 0
    
    def check_paper(x, y, n):
        nonlocal white, blue
        # Check if all squares are the same color
        color = paper[x][y]
        for i in range(x, x + n):
            for j in range(y, y + n):
                if paper[i][j] != color:
                    # If not, divide the paper into four and repeat the process
                    m = n // 2
                    check_paper(x, y, m)
                    check_paper(x, y + m, m)
                    check_paper(x + m, y, m)
                    check_paper(x + m, y + m, m)
                    return
        # If all squares are the same color, increase the count for that color
        if color == 0:
            white += 1
        else:
            blue += 1

    check_paper(0, 0, n)
    return white, blue

white,blue=count_colored_paper(N, paper)
print(white)
print(blue)