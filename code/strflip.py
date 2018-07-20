def strflip(s):
    """
    strflip: Flip a string
 
    Parameters
    ----------
    s : str
        String to reverse
 
    Returns
    -------
    flipped : str
        Copy of `s` with characters arranged in reverse order
    """
 
    flipped = ''
 
    # Starting from the last character in `s`,
    # add the character to `flipped`,
    # and proceed to the previous character in `s`.
    # Stop whenever we reach the first character.
 
    i = len(s)

    if i == 0:
        return ''
 
    while True:
        i = i-1
        char = s[i]
        flipped = flipped + char
 
        # stop if we have reached the first character:
        if char == s[0]:
           break
 
    return flipped
