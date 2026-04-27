# Valid Palindrome
# A phrase is a palindrome if, after converting all uppercase letters to lowercase and removing all non-alphanumeric characters, it reads the same forward and backward.
# Given a string s, return True if it is a palindrome, False otherwise.
# Input:  s = "A man, a plan, a canal: Panama"
# Output: True

# Input:  s = "race a car"
# Output: False

# Input:  s = "Was it a car or a cat I saw?"
# Output: True
# Constraints:

# Ignore spaces, punctuation, casing
# Try to solve it in O(n) time
# Bonus: can you do it with O(1) extra space?

def isPalindrome(text):
    cleaned = "".join(ch for ch in text.lower() if ch.isalnum())
    i, j = 0, len(cleaned) - 1
    while i <= j:
        if cleaned[i] != cleaned[j]:
            return False
        i += 1
        j -= 1
    return True  
            
if __name__ == '__main__':
    text = "A man, a plan, a canal: Panama"
    print(f"is palindrome: {isPalindrome(text)}")

