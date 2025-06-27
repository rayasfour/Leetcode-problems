"""
Problem Statement
Given a sorted array, create a new array containing squares of all the numbers of the input array in the sorted order.

Example 1:

Input: [-2, -1, 0, 2, 3]
Output: [0, 1, 4, 4, 9]
Example 2:

Input: [-3, -1, 0, 1, 2]
Output: [0, 1, 1, 4, 9]
Constraints:

1 <= arr.length <= 104
-104 <= arr[i] <= 104
arr is sorted in non-decreasing order.
"""
class Solution:
  def makeSquares(self, arr):
    n = len(arr)
    squares = [0 for x in range(n)]

    highestsquareIndx = n - 1
    left = 0
    right = n - 1

    while left <= right:
      leftSquare = arr[left]* arr[left]
      rightSquare = arr[right]* arr[right]

      if leftSquare >= rightSquare:
        squares[highestsquareIndx] = leftSquare
        left += 1
        
      else:
        squares[highestsquareIndx] = rightSquare
        right -= 1

      highestsquareIndx -= 1

    return squares
