import cv2

def resize_image(image, width, height):
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    resized_image = cv2.resize(image, dsize=(width, height), interpolation=cv2.INTER_CUBIC)

    resized_image = cv2.cvtColor(resized_image, cv2.COLOR_RGB2BGR)

    return resized_image
