ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
NOM = 851
DENOM = 500


def encode(in_bytes: bytes) -> str:
    in_bytes = list(in_bytes)
    in_length = len(in_bytes)
    out_length = (in_length * NOM + DENOM - 1) // 500

    out_string = ""
    for _ in range(out_length):
        accumulator = 0
        for i in range(in_length-1, -1, -1):
            full_value = (accumulator * 256) + int(in_bytes[i])
            full_value_m26 = full_value % 26
            b26_value = (full_value - full_value_m26) // 26
            in_bytes[i] = b26_value
            accumulator = full_value_m26
        out_string += ALPHABET[accumulator]

    return out_string


if __name__ == "__main__":
    str = "Hello base24"
    str_encoded = bytes(str, "UTF-8")

    print(encode(str_encoded))
