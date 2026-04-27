# Longest Substring Without Repeating Characters
# Given a string s, find the length of the longest substring without repeating characters.
# Input:  s = "abcabcbb"
# Output: 3  # "abc"

# Input:  s = "bbbbb"
# Output: 1  # "b"

# Input:  s = "pwwkew"
# Output: 3  # "wke"

# Input:  s = ""
# Output: 0

def findWindow(text):
    items = list(text)
    i = 0
    j = 0
    best = 0
    seen = set()

    while j < len(items):
        if items[j] not in seen:            
            seen.add(items[j])
            best = max(best, len(seen))
            print(f"best: {best} seen: {seen}")
            j += 1
        else:
            seen.remove(items[i])
            print(f"seen: {seen}")
            i += 1

    return best                      

if __name__ == "__main__": 
    input = "abcabcbb"
    print(input)
    print(findWindow(input))