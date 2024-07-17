import sys

teams = list(map(int, input().split()))
minDiff = sys.maxsize

def getMinimumDifference(teams):

    def makeTeams(selected, remaining):
        global minDiff
        if len(selected) == 6:
            team1 = selected[0:2]
            team2 = selected[2:4]
            team3 = selected[4:6]
            
            sum1 = sum(team1)
            sum2 = sum(team2)
            sum3 = sum(team3)
            
            diff = max(sum1, sum2, sum3) - min(sum1, sum2, sum3)

            if diff < minDiff :
                minDiff = diff

            return
        
        for i in range(len(remaining)):
            makeTeams(selected + [remaining[i]], remaining[:i] + remaining[i+1:])
    
    makeTeams([], teams)
    return minDiff

print(getMinimumDifference(teams))