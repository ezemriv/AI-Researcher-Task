# Time-Series Imputation: Fast Implementation of State-of-the-Art Methods  

## Introduction  
**Missing data in time series is a pervasive challenge** in real-world applications such as climate monitoring, healthcare, and IoT systems. Causes range from **sensor failures, communication issues, to data corruption**, often resulting in **irregular and non-random missingness**.  

Recent research emphasizes that **imputation quality directly impacts downstream tasks** like forecasting and classification, with advanced models outperforming traditional methods — especially in **complex missingness patterns like MNAR (Missing Not at Random)**.  

Given this, the goal of this project was to **evaluate imputation methods** under realistic conditions using **MCAR and MNAR simulations** and implement a **fast, yet powerful solution** leveraging modern tools like **PyGrinder** and **PyPOTS**, aligned with recent benchmarks such as **TSI-Bench (Du et al., 2024)**.

---

## 📊 Results Presentation  
I’ve compiled my methodology and results into a **PowerPoint presentation**, which you can view here:  
👉 [Presentation Link](https://1drv.ms/p/c/53632949597850a7/ERWML11yCuNIlgW-rCRt2EQBq_NnqEPxs8jXydLblKmRpQ?e=8o61Hk)  

**Feel free to review and reach out — I welcome any feedback or discussion.**

---

## Objectives  
- Simulate **realistic missing data** using **PyGrinder** with **MCAR and MNAR** mechanisms.  
- Apply and compare imputation methods: **mean**, **interpolation**, **KNN**, and **SAITS (PyPOTS)**.  
- Benchmark against **ground truth** and evaluate **forecasting performance** post-imputation using **LightGBM**.  
- Deliver a **reproducible and fast implementation** aligned with **cutting-edge research** on time series imputation.

---

## Key Features  
- **Quick deployment** using ready-to-use tools for missingness simulation (PyGrinder) and **deep learning** imputation (PyPOTS).  
- **10-min resolution climate data**, analyzed via **EDA** to understand noise, seasonality, and correlations.  
- Resampled data to **6-hour intervals** to better capture seasonal patterns and reduce noise.  
- Compared **8 datasets** (original, corrupted, imputed) for both **imputation error** and **forecast accuracy**.

---

## Results Summary  
- **Interpolation and SAITS** were top performers; **SAITS excelled in MNAR scenarios**.  
- **KNN struggled with MNAR**, but improved post-resampling.  
- In some cases, **forecast RMSE was lower with imputed data**, indicating possible **denoising effects**.

---

## Future Work  
- Test **polynomial/spline interpolation** for more flexible statistical imputation.  
- Explore additional **PyPOTS models** (e.g., diffusion-based, transformer-based).  
- Evaluate **diverse MNAR patterns** and **varying missingness levels**.  
- Build a **more complex forecasting model** to rigorously test **high-frequency (10-min) data**.

---

## References  
- Du et al. (2024). *TSI-Bench: Benchmarking Time Series Imputation.* arXiv:2406.12747.  
- Du et al. (2023). *SAITS: Self-Attention-based Imputation for Time Series.* Expert Systems with Applications.  
- Qian et al. (2024). *Frequency-aware Generative Models for Time Series Imputation (FGTI).* OpenReview: n2dvAKKQoM.