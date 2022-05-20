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


if __name__ == "__main__":
    source = "4A2A7852EB17D80493BFB526187F5504564244581F600D649AF81B28627B9DF08F7378BB4B0C9C75AFE0AF8342A86154CDC7AE41BD51EFE291FD9B816B92506A1622228B073D08B92F3CA83808380362A8F6C4D60875AA268247504825A094CDE117FCD4F3188090D881EF82DFF3102F0D745E269DBF9895FFE4239FFEB51AB4"
    expected = "KMUZPLCLWJWJENIQYWEMJMRSQIRNGIKCUIQNDFCNNUSIVIDSGVOOMZLVTVNNLJIHXPQLUMKGSACYWRORIRQGULTWDHVEJBZUHVYVVDIJXIBZJZKHCAEAEYFEFRBXTCXXFHUXIQNHTBJGFWGUCVMLDUSJXJZGRVJRMEGBUSYCAZSABIKFLVIHXNVOHVFPWDVKXBFJRXGVCPFGNEIYAPGFGWPPHL"
    
    data = bytes.fromhex(source)
    encoded = encode(data)
    assert encoded == expected

    data1 = decode(encoded)
    assert data1 == data
