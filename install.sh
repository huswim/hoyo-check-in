#!/bin/bash

# 0.  LTOKEN_V2, LTUID_V2 입력
read -p "LTOKEN_V2=" LTOKEN_V2
read -p "LTUID_V2=" LTUID_V2

docker run --rm --name "hoyo-check-in" -e LTOKEN_V2=$LTOKEN_V2 -e LTUID_V2=$LTUID_V2 ghcr.io/huswim/hoyo-check-in:latest

# 1. 서비스 파일 생성
cat <<EOF >/etc/systemd/system/hoyo-check-in.service
[Unit]
Description=Start hoyo-check-in Docker Container
Requires=docker.service
After=docker.service

[Service]
Type=oneshot
ExecStart=/usr/bin/docker run hoyo-check-in

[Install]
WantedBy=multi-user.target
EOF

# 2. 타이머 파일 생성
cat <<EOF >/etc/systemd/system/hoyo-check-in.timer
[Unit]
Description=Start hoyo-check-in Docker Container Daily

[Timer]
OnCalendar=*-*-* 06:00:00
Persistent=true

[Install]
WantedBy=timers.target
EOF

# 3. systemd 재로드
systemctl daemon-reload

# 4. 타이머 활성화 및 시작
systemctl enable hoyo-check-in.timer
systemctl start hoyo-check-in.timer

echo "Docker container start timer has been created and activated."
