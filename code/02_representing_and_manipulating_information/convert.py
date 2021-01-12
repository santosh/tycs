hex_bin_map = {
    "0": "0000",
    "1": "0001",
    "2": "0010",
    "3": "0011",
    "4": "0100",
    "5": "0101",
    "6": "0110",
    "7": "0111",
    "8": "1000",
    "9": "1001",
    "a": "1010",
    "b": "1011",
    "c": "1100",
    "d": "1101",
    "e": "1110",
    "f": "1111"
}


def get_key_from_value(value, dict):
    for key, val in dict.items():
        if val == value:
            return key


def hex_to_binary(hex_num: str) -> str:
    """hex number is supposed to be passed as 0x at start."""

    hex_num = hex_num[2:]

    binary = ""

    for char in hex_num.lower():
        binary += hex_bin_map[char]

    return binary

def bin_to_hex(bin_num: str) -> str:
    """bin_num should be a padded binary."""
    
    # check if length of input is divisible by 4 or raise error
    if len(bin_num) % 4 != 0:
        raise ValueError("binary number must be padded")

    hex_num = ""

    bin_nums = [(bin_num[i:i+4]) for i in range(0, len(bin_num), 4)] 

    for num in bin_nums:
        hex_num += get_key_from_value(num, hex_bin_map)

    return "0x"+hex_num


