

# Variables to keep track of the screenshot filenames
counter_1 = 0
counter_2 = 1
counter_3 = 1

# Initialize the coordinates for the area to capture
x1, y1, x2, y2 = 0, 0, 0, 0

# DataFrame to hold the Excel data
data_df = None
current_row = 0

# Specify the folder where you want to save the screenshots
save_folder = "screenshots"

# Create the folder if it doesn't exist
if not os.path.exists(save_folder):
    os.makedirs(save_folder)
