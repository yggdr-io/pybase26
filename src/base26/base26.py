NOM = 851
DENOM = 500


def encode(s: bytes) -> str:
    s = bytearray(s)
    out = ""
    out_length = (len(s) * NOM + DENOM - 1) // DENOM

    for _ in range(out_length):
        accumulator = 0
        for i in range(len(s) - 1, -1, -1):
            full_value = (accumulator * 256) + int(s[i])
            full_value_m26 = full_value % 26
            b26_value = (full_value - full_value_m26) // 26
            s[i] = b26_value
            accumulator = full_value_m26
        # 0 -> A, 1 -> B, ..., 25 -> Z
        out += chr(accumulator + 65)

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
