from cryptosteganography import CryptoSteganography

def encode_message(image_path, message, output_path, password):
    # Create a CryptoSteganography object
    crypto_steganography = CryptoSteganography(password)
    
    # Encode the message into the image
    crypto_steganography.hide(image_path, output_path, message)
    print(f"Message encoded and saved to {output_path}")

def decode_message(image_path, password):
    # Create a CryptoSteganography object
    crypto_steganography = CryptoSteganography(password)
    
    # Decode the message from the image
    message = crypto_steganography.retrieve(image_path)
    print(f"Decoded message: {message}")

def main():
    # User choice
    choice = input("Enter 'encode' to encode a message or 'decode' to decode a message: ").strip().lower()
    
    if choice == 'encode':
        image_path = input("Enter the path to the input image file: ").strip()
        message = input("Enter the message to encode: ").strip()
        output_path = input("Enter the path to save the encoded image file: ").strip()
        password = input("Enter a password to use for encryption: ").strip()
        encode_message(image_path, message, output_path, password)
    elif choice == 'decode':
        image_path = input("Enter the path to the encoded image file: ").strip()
        password = input("Enter the password used for encryption: ").strip()
        decode_message(image_path, password)
    else:
        print("Invalid choice. Please enter 'encode' or 'decode'.")

if __name__ == "__main__":
    main()
