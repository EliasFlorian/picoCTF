def convert_to_hex(filename):
    try:
        with open(filename, 'r', encoding="utf-8") as file:
            contents = file.read()
        
        hex_representation = ''.join([hex(ord(c)).lstrip("0x") for c in contents])
        
        # Convert hex representation back to ASCII
        ascii_representation = bytes.fromhex(hex_representation).decode('utf-8')
        print(ascii_representation)
    
    except FileNotFoundError:
        print(f"Error: The file {filename} was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    convert_to_hex("enc")

