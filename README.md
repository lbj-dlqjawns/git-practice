# git-practice

Git 및 GitHub 사용을 연습하기 위한 간단한 Python 단위 변환 프로젝트입니다.

## 프로젝트 구성
- `main.py`: 명령행 단위 변환 프로그램
- `converter.py`: 길이와 온도 변환 함수
- `tests/test_converter.py`: `unittest` 테스트
- `examples.md`: 실행 예제
- `CONTRIBUTING.md`: 프로젝트 기여 안내
- `.gitignore`: Python 캐시 및 로컬 환경 파일 제외

## 실행 방법

```bash
python main.py km-to-mi 10
python main.py c-to-f 25
python -m unittest discover -s tests
```

## 과제 체크리스트
- [x] 저장소 이름: `git-practice`
- [x] README.md / .gitignore 포함
- [x] 5개 이상 파일
- [x] 5개 이상 커밋
- [x] GitHub 공개 저장소에 업로드
