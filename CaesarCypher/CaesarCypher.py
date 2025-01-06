alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

# def encrypt(original_text, shift_amount):
#     result_text = ""
#     for letter in original_text:
#         shifted_position = alphabet.index(letter) + shift_amount
#
#         shifted_position %= len(alphabet)
#         result_text += alphabet[shifted_position]
#     print(result_text)
#
# encrypt(text, shift)
#
# def decrypt(original_text, shift_amount):
#     decrypted_word = ""
#     for letter in original_text:
#         position_shift = alphabet.index(letter) - shift_amount
#
#         if position_shift < 0:
#             position_shift += len(alphabet)
#         decrypted_word += alphabet[position_shift]
#     print(decrypted_word)

# decrypt(text, shift)


def caesar(original_text, shift_amount, action):
    result_text = ""

    for letter in original_text:


        if action == "decode":
            shift_amount *= -1 # Subtracts instead of multiplies

        shift_amount = alphabet.index(letter) + shift_amount
        shift_amount %= len(alphabet)
        result_text += alphabet[shift_amount]

    print(f"Here is the {action}d result: {result_text}")

caesar(text, shift, direction)