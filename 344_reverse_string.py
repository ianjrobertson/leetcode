class Solution:
    def reverseString(self, s: List[str]) -> None:
        left = 0
        right = len(s) - 1
        swap_char = ''

        while left < right:
            swap_char = s[left]
            s[left] = s[right]
            s[right] = swap_char

            left += 1
            right -= 1
    
        
