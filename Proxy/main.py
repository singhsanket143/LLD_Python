from ProxyImage import ProxyImage

def main():
    image1 = ProxyImage("HighResPhoto1.jpg")
    image2 = ProxyImage("HighResPhoto2.jpg")

    # Image is loaded and displayed only when the display method is called
    image1.display()  # This will load and display the image
    image1.display()  # This will only display the image without loading

    image2.display()  # This will load and display the image

if __name__ == "__main__":
    main()
