import cv2


def percentage_of_red_pixels(image):
    bgr_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # Create mask where pixels match red color range
    mask = cv2.inRange(bgr_image, (0, 0, 100), (100, 100, 255))

    # number of red pixels
    red_pixel_count = cv2.countNonZero(mask)

    # total pixels in the image
    total_pixels = image.shape[0] * image.shape[1]

    # percentage of red pixels
    percentage_red = (red_pixel_count / total_pixels) * 100

    return percentage_red


# Load original image
image = cv2.imread('Image_Q1.PNG')
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
red = cv2.imread('Image_Q1.PNG')

# Load image in grayscale, 0 flag means grayscale
gray = cv2.imread('Image_Q1.PNG', 0)

# do thresholding
_, thresholded_image = cv2.threshold(gray, 175, 255, cv2.THRESH_BINARY_INV)

# Invert  image so that teeth white and background black
segmented_teeth = cv2.bitwise_not(thresholded_image)

# Find the maximum intensity value , we don't need other returned values so just use placeholder '_'
_, max_val, _, _ = cv2.minMaxLoc(image)

# Replace all  brightest intensity pixels with red pixels
height, width = image.shape[:2]
for y in range(height):
    for x in range(width):
        if image[y, x] == max_val:
            red[y, x] = (0, 0, 255)  # Set to red (BGR format)

# Display the result
cv2.imshow('Original', image)
cv2.imshow('Segmented Teeth', segmented_teeth)
cv2.imshow('Brightest Pixel Highlighted', red)

red_percentage = percentage_of_red_pixels(red)
print("Percentage of red pixels:", red_percentage)

# this is just so that the windows close when any key is pressed
cv2.waitKey(0)
cv2.destroyAllWindows()
