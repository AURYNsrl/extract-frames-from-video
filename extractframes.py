import cv2
import os
from pathlib import Path
import argparse

def extract_frames(video_path, output_dir, step):
    cap = cv2.VideoCapture(video_path)

    if not cap.isOpened():
        print(f"Errore: impossibile aprire il video {video_path}")
        return

    Path(output_dir).mkdir(parents=True, exist_ok=True)

    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    print(f"Totale frame nel video: {total_frames}")

    frame_idx = 0
    saved_idx = 0

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        if frame_idx % step == 0:
            filename = f"frame_{saved_idx:06d}.jpg"
            filepath = os.path.join(output_dir, filename)
            cv2.imwrite(filepath, frame)
            print(f"Salvato: {filepath}")
            saved_idx += 1

        frame_idx += 1

    cap.release()
    print(f"Completato! Frame salvati: {saved_idx}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Estrai frame da un video ogni N frame.")
    parser.add_argument("--video", type=str, required=True, help="Percorso al file video")
    parser.add_argument("--step", type=int, default=30, help="Ogni quanti frame salvare un'immagine")
    parser.add_argument("--output_dir", type=str, default="frames", help="Cartella di output per i frame estratti")
    args = parser.parse_args()

    extract_frames(args.video, args.output_dir, args.step)
