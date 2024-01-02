# Investigation of Visual Fatigue in Real-Time, Based on the Computer Vision Methods

<aside>
시각 피로 측정을 위한 실시간 방식의 도입과 추출된 데이터의 타당성 검증 및 영상의 데이터에 기반한 시각 피로 변화 검증

</aside>

> **Employed Stacks** 
 `Psychopy` `OpenCV` `Pandas` `Numpy` `Pingouin` `Scikit-learn` `Matplotlibs` `Seaborn`
> 

# Main Ideas

![ML.png](Investigation%20of%20Visual%20Fatigue%20in%20Real-Time/ML.png)

1. **Joystick을 활용하여 영상 시청 중 발생되는 시각피로의 실시간 평가 방법 제안 및 데이터 추출 (Dynamic rating)**
2. **Optical Flow & V-value in HSV를 활용한 영상 모션, 밝기 정보 추출 및 실시간 시각 피로와의 관계 분석**
3. **Statistical Analysis를 통한 데이터간 차이 및 관계성 증명** 
4. **Sliding Window Analysis를 통한 시각피로의 실시간 변화 증명**
5. **Optical flow, V-value애 기반하여 ML model을 활용 실시간 시각 피로 예측**

# Data Processing



1. **Motion Information** 
    
    → Shi-Tomasi 알고리즘을 기반으로 Conner Detection 
    
    → Lukas-Kanade 알고리즘을 기반으로 각 Frame당 Motion vector 추출
    
    → **Frame마다 추출된 Motion Vector 크기의 총합을 계산**
    
2. **Brightness Information** 
    
    → **모든 Frame의 평균 V-value 추출**
    
3. **Sliding Window** 
→ **30-seconds 길이의 Window를 Element (1-seconds)단위로 이동시며 데이터의 평균값을 추출**

# Results
1. **시각 피로를 실시간으로 측정하는 검증된 대안 제시**
2. **모션에 따른 시각 피로의 증가 양상의 차이를 증명**
3. **V-value, Optical flow를 Feature로 시각 피로 80% 이상 예측**
