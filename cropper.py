import cv2
import os
import tqdm

### Crops a given rectange from all images inside the folder "originals" and saves them with the same name to a folder named cropped

# Cropping dimensions
row_start = 123
row_end = 1013
col_start = 652
col_end = 1246

### Sample code. Use to finalize the cropping dimensions. Comment it afterwards
test_image = 'test.jpg' #image name (NOT inside the 'originals' folder)
img = cv2.imread(test_image)
cut_image = img[row_start:row_end,col_start:col_end]
cv2.imwrite("test_cropped.jpg",cut_image)


##############################################################################

"""
### Final Code. Uncomment and run once the cropping dimensions are set.

# Check "originals" folder exist
if not os.path.isdir("originals"):
    raise Exception('"originals" folder does not exist. Put images to crop inside the folder with this name only.')

# Check if "cropped" folder exist; if not, create it 
if not os.path.isdir("cropped"):
    os.mkdir("cropped")

for data in os.walk('originals'):
    for image_name in tqdm.tqdm(data[2]):

        # Read Image
        img = cv2.imread("originals/"+image_name)

        # Read Image Size
        rows, cols, __ = img.shape

        # Check if dimensions within image size
        if row_end > rows:
            print("row crop size greater than image row size")
            break
        if col_end > cols:
            print("col crop size greater than image col size")
            break

        # Crop Image
        cut_image = img[row_start:row_end,col_start:col_end]

        # Save Image
        cv2.imwrite("cropped/"+image_name,cut_image)
"""
