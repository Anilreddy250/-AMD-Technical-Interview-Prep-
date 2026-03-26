def long_prefix(strs):
    if not strs:  # Edge case: Empty list
        return ""
    
    # 1. Take the first word as the reference
    first_word = strs[0]
    prefix = ""
    
    for i in range(len(first_word)):
        char = first_word[i]
        
        # 2. Check this character against the same position in every other word
        for word in strs:
            # Check if we hit the end of a word or found a mismatch
            if i >= len(word) or word[i] != char:
                return prefix  # Return whatever we built so far
        
        # 3. If it matches in all words, add it to our prefix
        prefix += char
        
    return prefix

# Test
print(long_prefix(["flower", "flow", "flight"])) # Output: "fl"
print(long_prefix(["dog", "racecar", "car"]))    # Output: ""
