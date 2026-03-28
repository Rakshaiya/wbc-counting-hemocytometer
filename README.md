# WBC Counting Using Hemocytometer

A Python-based computer vision tool that automatically detects and counts White Blood Cells (WBCs) in hemocytometer slide images using OpenCV's Hough Circle Transform.

---

## Problem Statement

Manual WBC counting in laboratory settings is time-consuming and prone to human error. This project automates the detection and counting process using image processing techniques, making it faster and more consistent.

---

## How It Works

1. Loads a hemocytometer slide image in grayscale
2. Applies the **Hough Circle Transform** to detect circular cell shapes
3. Counts the detected circles (WBCs)
4. Draws the detected circles on the image for visual validation
5. Displays the final count and annotated image

---

## Tech Stack

- **Python**
- **OpenCV** — image processing and circle detection
- **NumPy** — array operations

---

## Usage

1. Clone the repository:
```bash
git clone https://github.com/Rakshaiya/wbc-counting-hemocytometer.git
cd wbc-counting-hemocytometer
```

2. Install dependencies:
```bash
pip install opencv-python numpy
```

3. Place your hemocytometer image in the project folder and rename it `wbc.jpg` (or update the filename in the code)

4. Run the script:
```bash
python CODE.py
```

---

## Output

- Prints the total WBC count to the console
- Displays the slide image with detected cells highlighted in green circles

---

## Project Context

Developed as part of a university project at **Sathyabama Institute of Science and Technology, Chennai** (Oct 2024 – Dec 2024), focused on applying Python and computer vision to real-world biomedical problems.

---

## Author

**Rakshaiya Yadav G**
- GitHub: [@Rakshaiya](https://github.com/Rakshaiya)
- Email: rakshaiya115@gmail.com
