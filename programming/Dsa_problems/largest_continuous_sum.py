
def large_cont_sum(a):

    greater_sum = a[0] + a[1]
    curr_sum = a[0] + a[1]

    for i in range(2,len(a)):

        curr_sum = curr_sum + a[i]

        if curr_sum > greater_sum:

            greater_sum = curr_sum

    return greater_sum
    
#returned_sum = largest_sum([1,2,-1,3,4,10,10,-10,-1])
#print(returned_sum)

from nose.tools import assert_equal

class LargeContTest(object):
    def test(self,sol):
        assert_equal(sol([1,2,-1,3,4,-1]),9)
        assert_equal(sol([1,2,-1,3,4,10,10,-10,-1]),29)
        assert_equal(sol([-1,1]),0)
        print ('ALL TEST CASES PASSED!!')
        
#Run Test
t = LargeContTest()
t.test(large_cont_sum)