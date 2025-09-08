# pose.py
# Zeigt Workout Bild

from ultralytics import YOLO

# Lade das Modell
model = YOLO("yolo11n-pose.pt")  

# Lade das Bild
results = model(["Jogger.png"])  

# Ergebnisse verarbeiten
for result in results:
    boxes = result.boxes  # Boxenobjekt für Bounding-Box-Ausgaben
    masks = result.masks  # Maskenobjekt für die Ausgaben von Segmentierungsmasken
    keypoints = result.keypoints  # Schlüsselpunktobjekt für Pose-Ausgaben
    probs = result.probs  # Wahrscheinlichkeitsobjekt für Klassifikationsausgaben
    obb = result.obb  # Orientierte Boxenobjekte für OBB-Ausgaben
    result.show()  # Auf dem Bildschirm anzeigen
    result.save(filename="Pose.jpg")  # Auf die Festplatte speichern