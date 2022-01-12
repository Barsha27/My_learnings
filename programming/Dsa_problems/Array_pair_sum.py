
def pair_sum(ele,k):

    '''
    calculating the pair_sum of an array
    '''
    lst = []
    counter = 0  # counts the no of unique pairs we are getting
    for i in range(len(ele) - 1):


        if ele[i] + ele[i+1] == k:

            pair = (ele[i],ele[i+1])

            if pair not in lst: # checks the unique pair in the list

                lst.append(pair)
                counter += 1

    return counter

            

    #for i in lst:
        #print(i)


#pair_sum([2,2,2,2], 4)


from nose.tools import assert_equal

class TestPair(object):
    
    def test(self,sol):
        assert_equal(sol([1,9,2,8,3,7,4,6,5,5,13,14,11,13,-1],10),5)
        assert_equal(sol([1,2,3,1],3),1)
        assert_equal(sol([1,3,2,2],4),2)
        print('ALL TEST CASES PASSED!')
        
#Run tests
t = TestPair()
t.test(pair_sum)

