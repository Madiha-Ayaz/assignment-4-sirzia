import qrcode
import cv2

def generate_qr_code():
    data = input("Enter data to encode into QR code: ")
    qr = qrcode.make(data)
    filename = input("Enter filename to save QR (e.g., 'my_qr.png'): ")
    qr.save(filename)
    print(f"QR Code saved as {filename}")

def decode_qr_code():
    filepath = input("Enter image filename to decode (e.g., 'my_qr.png'): ")
    try:
        img = cv2.imread(filepath)
        detector = cv2.QRCodeDetector()
        data, bbox, _ = detector.detectAndDecode(img)
        if data:
            print("Decoded Data:", data)
        else:
            print("No QR Code found in the image.")
    except Exception as e:
        print("Error reading the image:", e)

def main():
    print("QR Code Generator and Decoder")
    print("1. Generate QR Code")
    print("2. Decode QR Code from image")
    choice = input("Enter your choice (1 or 2): ")

    if choice == '1':
        generate_qr_code()
    elif choice == '2':
        decode_qr_code()
    else:
        print("Invalid choice. Please enter 1 or 2.")

if __name__ == "__main__":
    main()
