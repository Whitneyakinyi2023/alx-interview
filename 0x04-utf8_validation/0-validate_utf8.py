#!/usr/bin/python3
"""UTF8 Validation"""


def validUTF8(data):
    """
    Checks if the given data is valid UTF-8 encoded.

    Args:
        data: A byte string or iterable of bytes.

    Returns:
        True if the data is valid UTF-8, False otherwise.
    """

    num_bytes = 0  # Number of bytes in the current UTF-8 character

    for byte in data:
        # Ensure byte is within the valid range (0-255)
        byte &= 0xFF

        # If we're starting a new UTF-8 character:
        if num_bytes == 0:
            # Determine the number of bytes based on the leading bits
            num_bytes = num_bytes_from_leading_bits(byte)

            # Handle single-byte characters (0xxxxxxx)
            if num_bytes == 0:
                continue

            # Ensure the number of bytes is valid (2-4)
            if num_bytes < 2 or num_bytes > 4:
                return False

        # For subsequent bytes, they must match the pattern 10xxxxxx
        elif not (byte & 0x80 and not (byte & 0x40)):
            return False

        # Decrease the count of bytes in the current UTF-8 character
        num_bytes -= 1

    # If all characters are valid, num_bytes should be 0 at the end
    return num_bytes == 0


def num_bytes_from_leading_bits(byte):
    """
    Determines the number of bytes
    in a UTF-8 character based on its leading bits.

    Args:
        byte: The first byte of a UTF-8 character.

    Returns:
        The number of bytes
        in the character, or 0 if it's a single-byte character.
    """

    num_bytes = 0
    while byte & 0x80:
        num_bytes += 1
        byte >>= 1
    return num_bytes
