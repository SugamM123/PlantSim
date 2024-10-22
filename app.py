import os
import random

# Configuration
detections_file = 'yolov5_custom/detections.txt'
moisture_threshold = {
    'rose': 30,
    'sunflower': 20,
    'daisy': 25
}

# Read detections from the file and store them in a list
def read_detections(file_path):
    detections = []
    with open(file_path, 'r') as file:
        for line in file:
            parts = line.strip().split()
            if len(parts) >= 2:
                label = parts[0]
                confidence = parts[1]
                detections.append({'label': label, 'confidence': confidence})
    return detections

# Get random moisture level
def get_moisture():
    return random.randint(0, 100)

# Determine if watering is needed based on moisture level
def should_water(plant_type):
    current_moisture = get_moisture()
    return current_moisture < moisture_threshold.get(plant_type), current_moisture

# Main function to process plant watering decisions
def process_plants():
    detections = read_detections(detections_file)
    for detection in detections:
        plant_type = detection['label']
        give_water, moisuture_level = should_water(plant_type)
        print(f"Plant: {plant_type}, Moisture: {moisuture_level}, Give Water: {give_water}")

# Execute the main function
if __name__ == "__main__":
    process_plants()