Image Processing Toolkit 2
**Author:** Sahil Minhas  

---

## 📘 Overview
The assignment explores various image processing techniques such as edge detection, connected component labeling, and iris segmentation using OpenCV and NumPy.  

Each task builds upon the previous one, demonstrating key principles in image analysis and feature detection.

---

Tasks

**Task 1 – Marr-Hildreth and Canny Edge Detection**
- Implemented the **Marr–Hildreth** edge detector using:
  - Gaussian smoothing
  - Laplacian filtering
  - Zero-crossing detection
- Used OpenCV’s built-in **Canny Edge Detector** for comparison.
- Compared both results to analyze the effect of edge thickness, noise, and detection accuracy.

---

**Task 2 – Connected Component Detection**
- Implemented **connected-component labeling** using a **BFS (queue-based)** region-growing algorithm.
- Used **8-connectivity** to identify distinct edge regions.
- Applied to both Marr–Hildreth and Canny edge maps from Task 1.
- Visualized results using random colors for each detected component.

**Outputs:**
- `img1_connected_marr_hildreth.tif`  
- `img1_connected_canny.tif`

---

### 👁️ **Task 3 – Iris Segmentation**
- Applied **Gaussian smoothing** and **Canny edge detection** for preprocessing.
- Detected:
  - **Pupil** (inner circle)
  - **Iris** (outer circle)
- Used **Hough Circle Transform** (`cv2.HoughCircles`) for circle detection.
- Overlaid both circles on the original image and saved results.

**Outputs:**
- `eye#_edges.tif`  
- `eye#_circles.tif`  
(where `#` = 1 to 5)

---
