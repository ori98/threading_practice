from concurrent.futures import ThreadPoolExecutor, as_completed
from time import sleep
from datetime import datetime


# Function to process the image
def process_image(img_id: int):
    print(f"Processing image: {img_id} at time: {datetime.now()}")
    sleep(5)
    print(f"Processed image: {img_id} at time: {datetime.now()}")
    return f"Result of process_image for image {img_id}"


# Function to execute the task
def exec_process_img():
    images = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    # Set max_workers as 3 since we can only process 3 images at a time
    with ThreadPoolExecutor(max_workers=3) as executor:
        # This sends all the images for processing
        # Blocks until all (3 in this case) images have been processed
        # processed_image = executor.map(process_image, images)

        # To process any completed image as we go
        futures = [executor.submit(process_image, img_id) for img_id in images]

        # We print the result
        for future in as_completed(futures):
            print(f"DONE: {future.result()} received at time: {datetime.now()}")

    # return list(processed_image)


if __name__ == "__main__":
    processed_images = exec_process_img()
    # print(processed_images)
