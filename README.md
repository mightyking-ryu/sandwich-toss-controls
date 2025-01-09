# Sandwich Toss Controls

## Table of Contents
- [Inspiration](#inspiration)
- [Scenario](#scenario)
- [Installation](#installation)
- [Program Screenshots](#program-screenshots)
- [Usage](#usage)
- [Simulation Rules](#simulation-rules)
- [Unimplemented Features](#unimplemented-features)
- [Project Structure](#project-structure)
- [License](#License)

## Inspiration
MIT 물리 강의 유튜브 영상에서 소개된 창의적인 교육용 프로그램을 보고 영감을 받았습니다. 아래는 해당 강의의 링크와 썸네일 이미지입니다.

[8.01x - Lect 22 - Kepler's Laws, Elliptical Orbits, Satellites, Orbital Changes](https://youtu.be/9wDAm-dlht4?si=1gOljDJfHqsrDUtq&t=2616)

![Lecture Thumbnail 1](https://od.lk/s/MzhfMjgyOTI5Njlf/thumbnail%201.png)
![Lecture Thumbnail 2](https://od.lk/s/MzhfMjgyOTI5NzBf/thumbnail%202.png)
![Lecture Thumbnail 3](https://od.lk/s/MzhfMjgyOTI5Njhf/thumbnail%203.png)

이 영상의 demonstration 부분에서 학생이 시연하고 있는 Sandwich Toss Controls 프로그램을 Python으로 구현해보자는 생각에서 시작되었습니다.

## Scenario
철수와 영희(강의 영상에서는 Marry and Peter)는 지구를 공전하고 있는 서로 다른 인공위성에 탑승해 있습니다. 영희는 아침에 만든 샌드위치를 철수에게 전달하고 싶습니다. 이를 위해 철수가 캐치할 수 있도록 궤도를 계산하여 정확한 속도로 샌드위치를 던져야 합니다.

이 프로젝트는 이러한 상상을 바탕으로, 사용자 입력에 따라 물리적인 궤도를 계산하고 시뮬레이션으로 시각화하는 교육용 프로그램입니다.

## Installation
### 방법 1: GitHub 리포지토리 클론
1. 리포지토리 클론:
   ```bash
   git clone https://github.com/mightyking-ryu/sandwich-toss-controls.git
   ```
2. 프로젝트 디렉토리로 이동:
   ```bash
   cd sandwich-toss-controls
   ```
3. 의존성 패키지 설치:
   ```bash
   pip install pillow pywin32
   ```
4. 애플리케이션 실행:
   ```bash
   python ./main.py
   ```

### 방법 2: 실행 파일 다운로드
1. [여기](https://github.com/mightyking-ryu/sandwich-toss-controls/releases)에서 최신 `.exe` 파일을 다운로드합니다.
2. 다운로드한 파일을 실행합니다.

### 주의사항
- 윈도우 환경에서만 실행 가능합니다.
- exe 파일의 경우 로딩 시간이 길 수 있습니다.


## Program Screenshots
1. **초기 화면**
   ![프로그램 초기 화면](https://od.lk/s/MzhfMjgyOTI4ODZf/screenshot%201.png)
2. **궤도 설정**
   ![궤도 및 우주선 설정 화면](https://od.lk/s/MzhfMjgyOTI4ODRf/screenshot%202.png)
3. **시뮬레이션 진행**
   ![시뮬레이션 진행](https://od.lk/s/MzhfMjgyOTI4ODVf/demonstration.gif)

## Usage
1. 애플리케이션을 실행합니다.
2. 시뮬레이션 매개변수를 조정합니다:
3. **Prepare Toss 버튼**을 클릭한 후 **시작 버튼(재생 버튼)** 을 클릭합니다.
4. 다양한 입력값을 시도하며 결과를 탐구해보세요.

## Simulation Rules
- 항상 **Prepare Toss 버튼**을 클릭한 후 시뮬레이션을 시작해야 합니다.
- **Auto 성공 루트**를 사용하면 샌드위치를 정확한 속도로 던질 수 있으며, 수동으로 매개변수를 입력할 경우 샌드위치를 전달하지 못할 수 있습니다.
- 주요 매개변수:
   - `Na`: 위성의 공전 횟수
   - `Ns`: 샌드위치의 공전 횟수
   - `Vs`: 샌드위치 속도 (던진 직후 속도 = 영희의 속도 + 던지는 속도)
   - `Separation`: 두 위성 간 위상 차이 (위성 공전 주기 `T`의 비율로 측정, 예: 0.1 = 0.1T)
   - `궤도`: 타원 궤도의 이심률 (0, 0.1, 0.2, 0.4 중에서 선택)
   - `지구중심으로부터 거리`: 위성이 지구와 가장 가까운 지점(근일점)에서의 거리
- 샌드위치가 지구와 충돌하는 조건은 대기를 무시하고 반지름 6400km를 기준으로 합니다.

## Unimplemented Features
- 위성과 샌드위치 궤도를 점선으로 시각화하는 기능
- 애니메이션 속도 조절
- 정지 버튼과 초기화 버튼
- 텍스트 출력 박스

## Project Structure
```
sandwich-toss-controls/
├── source/                # 이미지 소스
├── test/                  # 테스트 코드
├── LICENSE                # 라이선스 파일
├── README.md              # 프로젝트 설명 파일
├── ellipse.py             # 타원 궤도 클래스
└── main.py                # 메인 실행 파일
```

## License
이 프로젝트는 MIT 라이선스에 따라 배포됩니다.

---
