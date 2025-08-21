# Parcel Dimension Estimation using Computer Vision

## 📌 Overview
This project demonstrates a **Proof of Concept (PoC)** for estimating parcel dimensions using **computer vision techniques**.  
Instead of relying on traditional sensors, we leverage **OpenCV and ArUco markers** to extract the **pixel-to-dimension ratio** and visualize results directly on screen.

---

## 🎯 Objective
- Automate parcel dimension measurement.
- Reduce reliance on manual tools and physical sensors.
- Provide a scalable vision-based approach for future logistics and supply chain automation.

---

## 🛠️ Proposed Solution Flow
1. **Input Capture**  
   - An image of a parcel with an ArUco marker placed beside it is taken as input.

2. **Marker Detection**  
   - The system detects the ArUco marker in the image using OpenCV.
   - Since the marker size is predefined (e.g., 5 cm × 5 cm), it acts as a **reference object**.

3. **Dimension-to-Pixel Ratio Calculation**  
   - The system computes the **conversion ratio** between real-world dimensions and pixel values.

4. **Dimension Estimation**  
   - Using the ratio, the approximate size of the parcel in pixels can be mapped to **real-world dimensions**.

5. **Visualization**  
   - The output is displayed on screen with bounding boxes and dimension annotations.

---

## 📊 Proof of Concept Deliverables
- **Input**: Static image with a parcel and an ArUco marker.  
- **Output**:  
  - Detected marker.  
  - Display of pixel-to-dimension ratio.  
  - Annotated visualization of results.  

---

## 🚀 Next Steps
- Extend to **real-time scanning** using a webcam.  
- Build a **hardware prototype** for real-world parcel scanning.  
- Incorporate **AI/ML models** for improved accuracy and adaptability.  
- Explore integration into **logistics workflows**.

---

## 📂 Applications
- Logistics and supply chain automation.  
- Smart warehouses.  
- Courier and delivery services.  
- E-commerce parcel management.  

---
