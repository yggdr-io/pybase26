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
        accumulator = 0
        for i in range(len(s) - 1, -1, -1):
            value = accumulator * 26 + (s[i] - 65)
            s[i] = value // 256 + 65
            accumulator = value % 256
        out.append(accumulator)

    # There may be an extra zero character at the end of this array.
    # If so, truncate to 128 bytes.
    if len(out) == 129 and out[128] == 0:
        del out[128]

    return bytes(out)
