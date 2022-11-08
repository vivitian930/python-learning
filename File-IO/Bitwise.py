def _int32_to_bytes(i):
    """Convert an integer to four bytes in little-endian format."""
    # &: Bitwise-and
    # >> : Right-shift
    return bytes((i & 0xff, 
                  i >> 8 & 0xff,
                  i >> 16 & 0xff,
                  i >> 24 & 0xff))
if __name__ =="__main__":
    a = _int32_to_bytes(i=1)
    print(a)
   

    
