class Spy :
    def __init__(self, codeName = "", score = 0) :
        self.codeName = codeName
        self.score = score

spys = []
for _ in range(5) :
    codeName, score = tuple(input().split())
    spy = Spy(codeName, int(score))
    spys.append(spy)

minScore = spys[0].score
idx = 0

for i in range(1, len(spys)) :
    if spys[i].score < minScore :
        minScore = spys[i].score
        idx = i

print(spys[idx].codeName + " " + str(spys[idx].score))