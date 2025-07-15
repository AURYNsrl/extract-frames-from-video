# 🖼️ Estrai frame da un video

Script Python che permette di estrarre frame da un file video, salvandoli come immagini ogni N frame.

---

## ✨ **Funzionalità**
- Estrae automaticamente tutti i frame o solo un frame ogni N (configurabile)
- Salva le immagini in una cartella di output dedicata
- Stampa a schermo il numero totale di frame e i frame salvati

---

## 📦 **Requisiti**
- Python 3.8+
- OpenCV

Installa la dipendenza necessaria con:
```bash
pip install opencv-python

---

## ▶️ **Come usare**
Dal terminale, posizionati nella cartella del progetto ed esegui:
python extractframes.py --video path/al/video.mp4 --step 30 --output_dir frames
--video : percorso al file video da elaborare (obbligatorio)
--step : salva un frame ogni N frame (default: 30)
--output_dir : cartella dove salvare i frame estratti (default: frames)

---

## ✅ **Esempio**
Per estrarre un frame ogni 50 frame dal video dolomiti.mp4 e salvarli nella cartella output_frames:
python extractframes.py --video dolomiti.mp4 --step 50 --output_dir output_frames

## 📂 **Output**
Nella cartella di output troverai i file:
frame_000000.jpg
frame_000001.jpg
frame_000002.jpg
...