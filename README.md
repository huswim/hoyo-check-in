# hoyo-check-in

붕괴 스타레일, 젠레스 존 제로 출석체크

## 사용법

### 주기적 실행

[install.sh 다운로드](/install.sh)

```bash
sudo ./install.sh
```

### 일회성 실행

1. .env 파일 작성

```
LTOKEN_V2=""
LTUID_V2=""
```

2. 첫 실행

```bash
docker run --name "hoyo-check-in" --env-file .env ghcr.io/huswim/hoyo-check-in:latest
```

3. 이후 실행

```bash
docker start hoyo-check-in
```
