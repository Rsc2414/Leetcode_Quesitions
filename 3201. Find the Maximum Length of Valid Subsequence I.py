class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        count_even = 0
        count_odd = 0
        for num in nums:
            if num % 2 == 0:
                count_even += 1
            else:
                count_odd += 1
        
        max_len_same_parity = max(count_even, count_odd)

        alt_odd_even_len = 0
        expected_parity_odd_even = 1 

        alt_even_odd_len = 0
        expected_parity_even_odd = 0

        for num in nums:
            current_parity = num % 2

            if current_parity == expected_parity_odd_even:
                alt_odd_even_len += 1
                expected_parity_odd_even = 1 - expected_parity_odd_even
            
            if current_parity == expected_parity_even_odd:
                alt_even_odd_len += 1
                expected_parity_even_odd = 1 - expected_parity_even_odd
        
        max_len_alternating_parity = max(alt_odd_even_len, alt_even_odd_len)

        return max(max_len_same_parity, max_len_alternating_parity)
