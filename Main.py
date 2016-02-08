from Channel import * 
from Process import * 
from SystemState import * 
def underApproximation(initState,K): # return False if there is an reachable bad state of size K 
    reachableList = []
    reachableList.append(initState)
    i=0
    while i != len(reachableList):
        state1,state2 = reachableList[i].post()
        print str(i) +" - "+str(reachableList[i]) # + "------" + str(state1) + "------" + str(state2)
        if len(state1.channels[0].data) <= K and len(state1.channels[1].data) <= K :
            if state1.automata == 3 : return False
            if state1 not in reachableList : reachableList.append(state1)
        if len(state2.channels[0].data) <= K and len(state2.channels[1].data) <= K :
            if state2.automata == 3 : return False
            if state2 not in reachableList : reachableList.append(state2)
        i+=1
    print len(reachableList)
    return True


#test gamachannel
a=[Channel('0'),Channel('1'),Channel('10'),Channel('11'),Channel('110')]
print(Channel.printArray(SystemState.gamaChannel(4, a)))

#test alpha
print "test alpha ----------------------- "

test = SystemState([Process(1,1),Process(2,1)],1,[Channel("110"),Channel("111")])
l  = test.alpha(2)
for i in xrange(0,len(l)):
    print str(i) + " => "+str(l[i])
print str(len(l))

#test gama
print "test gama ----------------------- "
g=SystemState.gama(3, l)
# print g
for i in xrange(0,len(g)):
    print str(i) + " => "+str(g[i])
print str(len(g))

#test underapproximation
print "test underapproximation ----------------------- "

test = SystemState([Process(1,1),Process(1,1)],1, [Channel(""),Channel("")])
test2 = SystemState([Process(1,2),Process(1,1)],1, [Channel(""),Channel("")])
print underApproximation(test, 2)