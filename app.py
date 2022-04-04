ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
NOM = 851
DENOM = 500


def encode(data: bytes) -> str:
    data = list(data)
    data_length = len(data)
    encoded_length = (data_length * NOM + DENOM - 1) // DENOM

    encoded = ""
    for _ in range(encoded_length):
        accumulator = 0
        for i in range(data_length-1, -1, -1):
            full_value = (accumulator * 256) + int(data[i])
            full_value_m26 = full_value % 26
            b26_value = (full_value - full_value_m26) // 26
            data[i] = b26_value
            accumulator = full_value_m26
        encoded += ALPHABET[accumulator]

    return encoded


def decode(encoded: str) -> bytes:
    data = bytearray()
    data_length = (len(encoded) * DENOM + NOM - 1) // NOM
    encoded_raw = [ALPHABET.index(ch) for ch in encoded]

    for _ in range(data_length):
        accumulator = 0
        for i in range(len(encoded_raw)-1, -1, -1):
            value = accumulator * 26 + (256 + (encoded_raw[i] % 256)) % 256
            encoded_raw[i] = value // 256
            accumulator = (256 + (value % 256)) % 256
        data.extend(accumulator.to_bytes(2, "big"))

    return data


if __name__ == "__main__":
    data = b"Hello base24"
    encoded = encode(data)
    data1 = decode(encoded)

    assert data1 == data
