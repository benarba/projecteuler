def ascii_to_str(l):
    return "".join([chr(x) for x in l])


with open("0059_cipher.txt", "r") as f:
    text_ascii = [int(x) for x in f.read().split(",")]

counter = 0
q = False
for i in range(ord("a"), ord("z") + 1):
    for j in range(ord("a"), ord("z") + 1):
        for k in range(ord("a"), ord("z") + 1):
            key = [i, j, k]
            decoded_ascii = []
            for l in range(len(text_ascii)):
                decoded_ascii.append(text_ascii[l] ^ key[l % 3])

            decoded_text = ascii_to_str(decoded_ascii)
            if (
                "the" in decoded_text.lower()
                and "and" in decoded_text.lower()
                and "of" in decoded_text.lower()
                and "it" in decoded_text.lower()
                and "has" in decoded_text.lower()
            ):
                print(f"key_ascii: {key}")
                print(f"key: {ascii_to_str(key)}")

                print(f"sum: {sum(decoded_ascii)}")
                print(f"text: {decoded_text}")
