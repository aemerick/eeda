"""
Question 0

Find out if a year is actually a leap year.

e.g. 2000 - leap year
e.g. 1800 - not a leap year
e.g. 1996 - leap year

"""


"""
Question 1

We need to parse file names

File names contain: date-notebook_id-author-depreciated.<file_extention>

081991-571983-evan-depreciated.txt
032591-748932-danica.php

We want a dictionary: {
												"date": <date>: str,
												"notebook_id": <notebook_id>: int,
                        "author": <author>: str,
                        "is_depreciated": <True>: bool,
                        "file_extension": <file_extension>: str
                      }
"""

# filename

def convert_to_dict(filename):
  l = filename.split('-')

  if len(l) > 4 or len(l) < 3:
    raise RuntimeError

  if not ('depreciated' in l[-1]):
    author  = str(l[-1].split('.')[-1])
    is_dep = False
  else:
    author = str(l[-2])
    is_dep = True

    d = { "date" : str(l[0]),
        "notebook_id" : int(l[1]),
        "author" : author,
        "is_depreciated" :  is_dep,
        "file_extension" : str(l[-1].split('.')[-1])
      }

    return d





"""
#Question 2
#two sum: https://leetcode.com/problems/two-sum/
#Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

#You may assume that each input would have exactly one solution, and you may not use the same element twice.

#You can return the answer in any order.
# * try to solve this problem in linear time
"""

# nums
# target

for i in range(len(num)):
    diff = target - nums[i]

    if diff in num:
        return nums[i], diff


for i in range(len(num)):
    diff = target - nums[i]

    for j in range(i+1, len(num)):
        if diff == num[j]:
            return i,j

#
# final solution... doesn't quite work but close
#
n = len(num)
diff = {}
for i in range(n):
    diff[target-nums[i]] = i

    if nums[i] in diff:
        return i, diff[nums[i]]

#
## actual answer
def twosum_answer():
    diff = {}
    for i in range(len(nums)):
        if nums[i] in diff:
            return [i, diff[nums[i]]]
        else:
            diff[target-nums[i]] = i


"""
# Question 3
# logo problem: https://www.hackerrank.com/challenges/most-commons/problem
# kinda here ? https://leetcode.com/problems/find-common-characters/
# * find 3 most common characters in a string
# * if any share a frequency, sort in alphabetical order
"""

# three most common strings
# can do with hash?
# l   is the input string

def threecommon(string : str) -> List[str]:
    """
    This does not pass 1 of hackerranks test cases.
    Does fine on the rest. But the one is locked, so I'm
    not quite sure what the issue is.
    Unless there is some edge case in the input I missed
    (e.g. string = '')
    """

    d = {}
    for s in string:
        d[s] = d.get(s,0) + 1

    l = sorted(d.items(), key = lambda x : x[1], reverse=True)

    #
    # Actually this is likely the issue. Only does one swap
    # need to implement a different sorting alg here to
    # do better. And make another hash counter to
    # stop looping through once we've identified at least 3
    # top characters AND have moved on to the next lowest count
    # (to make sure we've gone through and sorted all at equal count
    #  that could be ranked in top 3).
    #
    for i in range(len(l)-1):
        if (l[i][1] == l[i+1][1]) and (l[i][0] > l[i+1][0]):
            val  = l[i]
            l[i] = l[i+1]
            l[i+1] = val

    for i in range(3):
        print(l[i][0], l[i][1])
