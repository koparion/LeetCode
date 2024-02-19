def encode(self, strs: List[str]) -> str:
    new_string = ""  # Initialize an empty string to store the encoded result
    
    for i in strs:  # Iterate through each string in the input list
        new_string += str(len(i)) + " " + i  # Append the length of the current string followed by a space, then append the string itself
    
    return new_string  # Return the encoded string

def decode(self, s: str) -> List[str]:
    old_string = []  # Initialize an empty list to store the decoded strings
    i = 0  # Initialize a pointer to keep track of the current position in the encoded string
    
    while i < len(s):  # Iterate over the characters in the encoded string
        j = i  # Mark the starting index of the length of the current string
        
        while(s[j] != " "):  # Find the end index of the length by iterating until a space is encountered
            j += 1
        
        length = int(s[i:j])  # Extract the length of the current string from the encoded string and convert it to an integer
        i = j + 1  # Move the pointer to the starting index of the current string        
        j = i + length  # Calculate the end index of the current string        
        old_string.append(s[i:j])  # Extract the current string from the encoded string and append it to the decoded list
        i = j  # Move the pointer to the next index after the end of the current string
    
    return old_string  # Return the decoded list of strings
