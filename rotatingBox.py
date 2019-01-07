'''

You need to move a large rectangular box over a rough, hazardous surface. Since you don't have any tools to help you move it, your only option is to perform a series of 90 degree rotations (basically just repeatedly pushing the box over onto its side).

Every time you rotate the box, it hits the ground and some damage is done - the amount of damage depends on the fragility of the side of the box that it landed on, as well as the roughness of the ground in the region where it was dropped.

what it looks like

More specifically, we calculate the damage by multiplying the box's fragility by the ground's roughness for each pair of vertically adjacent cells. So for the box above, dropping it into its current position would cause a total of 4*7 + 0*4 + 5*9 = 73 damage. And the next turn will cause 5*7 + 3*0 + 4*7 = 63 damage.

Given boxWeakness, an array of strings representing how fragile the box is in each location, and surfaceRoughness, a string of digits representing how damaging each section of the surface is, your task is to find the total amount of damage the box will receive after being rotated across the entire surface

Note: The length of the surface might not perfectly fit the box; if there's some overhang on the last step, that part won't be damaged.
Example

For

boxWeakness = ["01",
               "21",
               "10"]
and surfaceRoughness = "39513695380152438476", the output should be fragileRotatingBox(boxWeakness, surfaceRoughness) = 56.

example

The total damage is 1*3 + 0*9 + 0*5 + 1*1 + 1*3 + 1*6 +0*9 + 0*5 + 2*3 + 1*8 + 1*0 + 0*1 + 0*5 + 1*2 + 1*4 + 1*3 + 0*8 + 0*4 + 2*7 + 1*6 = 56

Input / Output

[execution time limit] 4 seconds (py3)

[input] array.string boxWeakness

An array of strings representing a picture of the box, in terms of how vulnerable each part of it is.

Guaranteed constraints:
1 ≤ boxWeakness.length ≤ 9
1 ≤ boxWeakness[i].length ≤ 9
boxWeakness[i][j] ∈ {"0" - "9"}

[input] string surfaceRoughness

A string of digits representing how damaging the surface is in each location.

Guaranteed constraints:
0 ≤ surfaceRoughness.length ≤ 105
surfaceRoughness[i] ∈ {"0" - "9"}

[output] integer

An integer representing the total amount of damage done to the box while rotating it over the full length of the surface.

'''



def fragileRotatingBox(boxWeakness, surfaceRoughness):
    parts=[boxWeakness[-1],"".join([i[-1] for i in boxWeakness])[::-1],boxWeakness[0][::-1],"".join([i[0] for i in boxWeakness])]
    willcover=list(map(lambda x:len(x),parts))
    
    completeTurns=math.floor(len(surfaceRoughness)/sum(willcover))
    remainingTurn=len(surfaceRoughness)%sum(willcover)
    
    toCrop=completeTurns*sum(willcover)
    
    return findRemaining(parts,surfaceRoughness[toCrop:],willcover,remainingTurn)+findRepeatedly("".join(parts),surfaceRoughness)
    

    
def findRemaining(partsToRoll,bottomArea,lengthOfParts,manyTimes):
    if manyTimes==0:
        return 0
    IndexWecareAbout=checkCareAbout(lengthOfParts,manyTimes)

    try:
        overLap=partsToRoll[:IndexWecareAbout]
    except:
        pass
    
    overLap=[str(k) for k in overLap]
    overLap="".join(overLap)
    
    return sum([int(x)*int(y) for x,y in list(zip(overLap,bottomArea))])
 
    
def findRepeatedly(combinedStr,rough):
    result=0
    while len(rough)>=len(combinedStr):
        mylist=list(zip(rough,combinedStr))
        
        result = result + sum([int(x)*int(y) for x,y in mylist])
        
        rough=rough[len(combinedStr):]
        
    return result
        
def checkCareAbout(lst,num):
    if num==0:
        return 0
    count=0
    for i in range(len(lst)):
        if num<=0:
            return i
        num=num-lst[i]
   