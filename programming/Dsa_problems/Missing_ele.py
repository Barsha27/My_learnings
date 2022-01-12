
def finder(lst1,lst2):

    # sort the elements

    lst1.sort()
    lst2.sort()

    for i in range(len(lst1)):
        if i <= len(lst2) - 1:

            if lst1[i] == lst2[i]:

                continue
            else:

                return lst1[i]
                break

        else:

            return lst1[i+1]

            break


    
#a = finder([5,5,7,7],[5,7,7])
#print(a)

"""
RUN THIS CELL TO TEST YOUR SOLUTION
"""
from nose.tools import assert_equal

class TestFinder(object):
    
    def test(self,sol):
        assert_equal(sol([5,5,7,7],[5,7,7]),5)
        assert_equal(sol([1,2,3,4,5,6,7],[3,7,2,1,4,6]),5)
        assert_equal(sol([9,8,7,6,5,4,3,2,1],[9,8,7,5,4,3,2,1]),6)
        print('ALL TEST CASES PASSED')

# Run test
t = TestFinder()
t.test(finder)