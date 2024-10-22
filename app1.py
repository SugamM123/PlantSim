import random

# Configuration
detections_file = 'yolov5_custom/detections.txt'
moisture_threshold = {
    'rose': 30,
    'sunflower': 20,
    'daisy': 25
}

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

def get_moisture():
    return random.randint(0, 100)

def should_water(plant_type):
    current_moisture = get_moisture()
    return current_moisture < moisture_threshold.get(plant_type), current_moisture

def get_plant_data():
    detections = read_detections(detections_file)
    results = []
    for detection in detections:
        plant_type = detection['label']
        give_water, moisture_level = should_water(plant_type)
        results.append({
            'plant_type': plant_type,
            'moisture_level': moisture_level,
            'needs_water': give_water
        })
    return results

if __name__ == "__main__":
    plant_data = get_plant_data()
    print(plant_data)  # For testing