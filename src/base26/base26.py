ALFABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
ALFABET_LEN = len(ALFABET)
BYTE_VALUES = 256  # a byte represents 256 different values
NOM = 851
DENOM = 500


def encode(src: bytes) -> str:
    src = bytearray(src)
    out = ""
    out_length = (len(src) * NOM + DENOM - 1) // DENOM

    for _ in range(out_length):
        acc = 0  # accumulator
        for i in range(len(src) - 1, -1, -1):
            full_val = (acc * BYTE_VALUES) + int(src[i])
            full_val_mod = full_val % ALFABET_LEN
            src[i] = (full_val - full_val_mod) // ALFABET_LEN
            acc = full_val_mod
        out += ALFABET[acc]

    return out


def decode(s: str) -> bytes:
    s = bytearray(s, "ascii")
    out = bytearray()
    out_length = (len(s) * DENOM + NOM - 1) // NOM

    for _ in range(out_length):
        acc = 0  # accumulator
        for i in range(len(s) - 1, -1, -1):
            value = acc * ALFABET_LEN + (s[i] - ord(ALFABET[0]))
            s[i] = value // BYTE_VALUES + ord(ALFABET[0])
            acc = value % BYTE_VALUES
        out.append(acc)

    # There may be an extra zero character at the end of this array.
    # If so, truncate the last byte.
    if out[out_length-1] == 0:
        del out[out_length-1]

    return bytes(out)
