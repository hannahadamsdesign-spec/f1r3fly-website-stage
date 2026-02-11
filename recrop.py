#!/usr/bin/env python3
"""
Re-crop all team photos with consistent head sizing and positioning.
Goal: All heads roughly same size, top of head aligned near top of frame.
Target: face takes up ~45% of frame height, top of head at ~8% from top.
"""
import cv2
import numpy as np
import os

IMG_DIR = "/Users/hannahadams/Library/CloudStorage/Dropbox/01 ACTIVE WORK/F1R3FLY PROJECTS/02 F1R3FLY Website/08 Website Rebuild/images"
ORIG_DIR = os.path.join(IMG_DIR, "originals")
OUTPUT_SIZE = 600

TEAM_PHOTOS = [
    "team-greg-meredith.webp",
    "team-mike-stay.webp",
    "lilia-rusu.jpg",
    "nicolas-riddle.jpg",
    "team-hannah-adams.webp",
    "stephen-alexander.jpg",
    "ralph-benko.jpg",
    "daria-bohdanova.jpg",
    "dylon-edwards.jpg",
    "serhii-lypko.jpg",
    "christian-b-wells.jpg",
    "adam-vandervorst.jpg",
    "nazar-yanovets.jpg",
    "steven-preston.jpg",
    "andrii-stefaniv.jpg",
    "andrii-babentsev.jpg",
    "team-nash-foster.webp",
    "ihor-rudynskyi.jpg",
    "diana-yevitska.jpg",
    "aidan-stay.jpg",
    "oleksandr-kyryliuk.jpg",
]

face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)

def detect_face(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    for scale in [1.1, 1.15, 1.2, 1.3]:
        faces = face_cascade.detectMultiScale(gray, scaleFactor=scale, minNeighbors=4, minSize=(30, 30))
        if len(faces) > 0:
            areas = [w * h for (x, y, w, h) in faces]
            idx = np.argmax(areas)
            return faces[idx]
    return None


def crop_with_consistent_framing(img, face_rect):
    """
    Crop so that:
    - The face (detected rectangle) occupies a consistent fraction of the output
    - Top of the detected face box sits at a consistent position from top
    
    Strategy:
    - We want the face_height to be about 40% of the final crop height
    - We want the top of the face to be at about 12% from the top of the crop
      (leaving room for forehead/hair above the face detection box)
    """
    h, w = img.shape[:2]
    fx, fy, fw, fh = face_rect
    
    # Target: face height = 40% of crop, face top at 12% from crop top
    TARGET_FACE_RATIO = 0.40
    TARGET_FACE_TOP = 0.12
    
    # Calculate required crop size based on face height
    crop_size = int(fh / TARGET_FACE_RATIO)
    
    # Ensure crop_size doesn't exceed image dimensions
    crop_size = min(crop_size, w, h)
    
    # Calculate where top of crop should be so face top is at TARGET_FACE_TOP
    crop_top = int(fy - TARGET_FACE_TOP * crop_size)
    
    # Calculate horizontal center on face
    face_cx = fx + fw // 2
    crop_left = face_cx - crop_size // 2
    
    # Clamp to image bounds
    crop_top = max(0, min(crop_top, h - crop_size))
    crop_left = max(0, min(crop_left, w - crop_size))
    
    cropped = img[crop_top:crop_top + crop_size, crop_left:crop_left + crop_size]
    return cropped


def process_photo(filename):
    from pathlib import Path
    filepath = os.path.join(ORIG_DIR, filename)
    if not os.path.exists(filepath):
        print(f"  SKIP (not found): {filename}")
        return False
    
    img = cv2.imread(filepath)
    if img is None:
        print(f"  SKIP (can't read): {filename}")
        return False
    
    h, w = img.shape[:2]
    face = detect_face(img)
    
    if face is not None:
        fx, fy, fw, fh = face
        cropped = crop_with_consistent_framing(img, face)
        status = f"face {fw}x{fh} at ({fx},{fy})"
    else:
        # Fallback: center crop
        side = min(w, h)
        top = int(h * 0.05)
        top = min(top, h - side)
        left = (w - side) // 2
        cropped = img[top:top + side, left:left + side]
        status = "NO FACE - center crop"
    
    resized = cv2.resize(cropped, (OUTPUT_SIZE, OUTPUT_SIZE), interpolation=cv2.INTER_LANCZOS4)
    
    stem = Path(filename).stem
    output_path = os.path.join(IMG_DIR, stem + ".jpg")
    cv2.imwrite(output_path, resized, [cv2.IMWRITE_JPEG_QUALITY, 92])
    
    final_kb = os.path.getsize(output_path) // 1024
    print(f"  OK: {filename} ({w}x{h}) -> {OUTPUT_SIZE}x{OUTPUT_SIZE} [{status}] {final_kb}KB")
    return True


def main():
    print(f"Re-cropping {len(TEAM_PHOTOS)} photos with consistent head sizing...")
    print(f"Target: face=40% of frame, face top at 12% from top\n")
    
    success = 0
    for photo in TEAM_PHOTOS:
        if process_photo(photo):
            success += 1
    
    print(f"\nDone! {success}/{len(TEAM_PHOTOS)} processed.")

if __name__ == "__main__":
    main()
