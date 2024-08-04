from PIL import Image  # Import the Image class from the PIL library (Pillow)

def encrypt_image(image_path, save_path, key):
    """
    Encrypts an image by shifting the RGB values of each pixel by the specified key.
    
    Args:
        image_path (str): The file path of the image to be encrypted.
        save_path (str): The file path where the encrypted image will be saved.
        key (int): The value by which to shift the RGB values for encryption.
        
    Returns:
        None
    """
    try:
        # Open the image file
        image = Image.open(image_path)
    except IOError:
        # Print an error message if the image cannot be opened
        print(f"Error: Unable to open image at {image_path}")
        return  # Exit the function if there is an error

    # Load the pixel data of the image
    pixels = image.load()

    # Iterate over each pixel in the image
    for i in range(image.width):
        for j in range(image.height):
            # Get the RGB values of the current pixel
            r, g, b = pixels[i, j]
            # Encrypt the RGB values by adding the key and wrapping around using modulo 256
            encrypted_r = (r + key) % 256
            encrypted_g = (g + key) % 256
            encrypted_b = (b + key) % 256
            # Update the pixel with the encrypted values
            pixels[i, j] = (encrypted_r, encrypted_g, encrypted_b)
    
    # Save the encrypted image to the specified path
    image.save(save_path)
    # Print a message indicating that the encryption was successful
    print(f"Image encrypted and saved as {save_path}")
    # Display the encrypted image
    image.show()

def decrypt_image(image_path, save_path, key):
    """
    Decrypts an image by shifting the RGB values of each pixel back by the specified key.
    
    Args:
        image_path (str): The file path of the encrypted image to be decrypted.
        save_path (str): The file path where the decrypted image will be saved.
        key (int): The value by which to shift the RGB values for decryption.
        
    Returns:
        None
    """
    try:
        # Open the image file
        image = Image.open(image_path)
    except IOError:
        # Print an error message if the image cannot be opened
        print(f"Error: Unable to open image at {image_path}")
        return  # Exit the function if there is an error

    # Load the pixel data of the image
    pixels = image.load()

    # Iterate over each pixel in the image
    for i in range(image.width):
        for j in range(image.height):
            # Get the RGB values of the current pixel
            r, g, b = pixels[i, j]
            # Decrypt the RGB values by subtracting the key and wrapping around using modulo 256
            decrypted_r = (r - key) % 256
            decrypted_g = (g - key) % 256
            decrypted_b = (b - key) % 256
            # Update the pixel with the decrypted values
            pixels[i, j] = (decrypted_r, decrypted_g, decrypted_b)

    # Save the decrypted image to the specified path
    image.save(save_path)
    # Print a message indicating that the decryption was successful
    print(f"Image decrypted and saved as {save_path}")
    # Display the decrypted image
    image.show()

# Define file paths and encryption key
image_path = r'C:\Users\neele\Desktop\ai_image.webp'  # Path to the original image
encrypted_image_path = r'C:\Users\neele\Desktop\encrypted.webp'  # Path to save the encrypted image
decrypted_image_path = r'C:\Users\neele\Desktop\decrypted.webp'  # Path to save the decrypted image
encryption_key = 200  # Key to use for encryption and decryption

# Encrypt the image
encrypt_image(image_path, encrypted_image_path, encryption_key)

# Decrypt the image
decrypt_image(encrypted_image_path, decrypted_image_path, encryption_key)
