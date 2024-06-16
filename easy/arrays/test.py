def decode(message_file):
    pyramid_lines = []

    # Read the input file and extract the pyramid lines
    with open(message_file, 'r') as file:
        for line in file:
            line = line.strip().split(' ')
            pyramid_lines.append(line[1])

    # Extract the message words based on pyramid structure
    message_words = [pyramid_lines[i] for i in range(0, len(pyramid_lines)) if i * (i + 1) // 2 < len(pyramid_lines)]

    # Combine the message words into a string
    decoded_message = ' '.join(message_words)

    return decoded_message

# Example usage:
message_file = 'encoded_message.txt'
result = decode(message_file)
print(result)
