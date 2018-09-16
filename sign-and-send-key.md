# 공개키에 키사이닝 하여 원래 주인분께 보내기

키사이닝 파티가 끝나고 키사이닝을 하는 방법은 여러 가지가 있습니다. GPG 커멘드라인으로도 가능하고, caff 나 pius 등 키사이닝과 메일 전송을 자동화 하는 툴로도 가능합니다.
키사이닝을 할 때에는, 키사이닝 파티 행사 때 본인이 신원을 확인하여 인쇄물 등에 체크 표시한 사람의 키에만 키사이닝을 하여야 합니다.
신원 확인 없이 무조건적으로 키사이닝을 하시면 본인과 상대방의 키에 대한 신뢰도가 추락할 위험이 있습니다.

## gpg 명령행 사용

서명할 키를 키서버에서 불러옵니다
```bash
gpg --keyserver <키서버 주소> --recv-keys <상대방의 키ID 나 핑거프린트>
# 실행 예시
# gpg --keyserver keyserver.ubuntu.com --recv-keys 90F64A666F4E7620
```

다음 명령을 실행하여 서명 과정을 시작합니다.
```bash
gpg --local-user <서명에 사용할 본인의 키ID 나 핑거프린트> --sign-key <상대방의 키ID 나 핑거프린트>

# 실행 예시
# gpg --local-user 30B729F712138599 --sign-key 90F64A666F4E7620
```

- 상대방의 공개키에 담긴 UID 정보와 함께 서명을 하겠냐는(Really sign? (y/N)) 질문이 나옵니다.
- 표시된 UID를 확인했고, 모든 UID에 서명하려면, y를 누르고 일부 UID 만 서명하려면 n을 누릅니다.
- n을 선택한 경우, 서명할 UID 를 숫자로 선택하게 됩니다. 한 숫자씩 누르고 Enter 키를 눌러 선택합니다.
- 선택 후 서명을 하려면 sign 을 입력 후 Enter 를 누릅니다.
- 다시 서명을 하겠냐는 질문이 나오면 y를 누릅니다. 서명이 완료되면 save 를 입력 후 Enter 를 눌러 마칩니다.

### 서명된 공개키 돌려주기

#### 키서버에 바로 업로드 하기
가장 쉽고 간단한 방법 입니다. 다만 원래 주인과 사전 협의를 한 후 하는것이 좋습니다.
어떤 키서버에 업로드 할 지 정하신 후, 아래 명령으로 키서버에 바로 업로드 합니다.
그러면 원래 주인은 해당 키서버에서 본인의 공개키를 다시 불러와서 갱신하면 됩니다.

```bash
gpg --keyserver <키서버 주소> --send-keys <상대방의 키ID 나 핑거프린트>

# 실행 예시 : 90F64A666F4E7620 를 keyserver.ubuntu.com 에 업로드
# gpg --keyserver keyserver.ubuntu.com --send-keys 90F64A666F4E7620
```
#### 메일 등으로 보내기

보통은 원래 주인이 직접 불러오는 작업 등을 제어할 수 있도록, 메일 등으로 보내는 경우가 많습니다.
서명하신 상대방의 공개키를 내보내기 한 다음 메일이나 메신저로 공유하시면 됩니다.

공개키를 파일로 내보내기 하려면 아래 명령을 실행합니다
```bash
gpg --armor --export <상대방의 키ID 나 핑거프린트> > <원하는_파일명>.asc
```

원래 키 주인만이 불러오기 등을 할 수 있게 하려면, 원래 주인의 공개키로 암호화를 하여 공유하는 방법도 있습니다.
암호화는 선택사항 입니다.

```bash
gpg --armor --export <상대방의 키ID 나 핑거프린트> | gpg --encrypt -r <상대방의 키ID 나 핑거프린트> --armor --output <상대방의 키ID 나 핑거프린트>-signedBy-<본인의 키ID 나 핑거프린트>.asc
```

# 키사이닝된 본인의 공개키 불러오기

## 키서버를 통해 공유받는 경우

사전 협의를 통해 키사이닝된 키를 키서버에 올려달라고 요청하신 경우, 키서버에서 불러오기만 하시면 됩니다.

```bash
gpg --keyserver <키서버 주소> --recv-keys <본인의 키ID 나 핑거프린트>
# 실행 예시
# gpg --keyserver keyserver.ubuntu.com --recv-keys 90F64A666F4E7620
```

## 메일 등으로 공유받은 경우
- 메일 등 본문 자체가 PGP 키 블록이거나 암호화된 PGP 메시지인 경우 복사하여 별도 파일로 저장합니다.
- 파일로 첨부되어 온 경우 다운로드 합니다.
- 암호화 되지 않은 경우 바로 불러옵니다.
```bash
gpg --import <파일명>

# 실행 예 : gpg --import yourkey.asc
```

- 복호화가 필요한 경우 복호화 후 파이프를 걸어 바로 불러옵니다.
```bash
gpg --decrypt <파일명> | gpg --import

# 실행 예 : gpg --import your-encrypted-key.asc | gpg --import
```

- 필요한 경우 불러온 공개키를 키서버에 업로드 합니다.
```bash
gpg --keyserver <키서버 주소> --send-keys <본인의 키ID 나 핑거프린트>

# 실행 예시 : 90F64A666F4E7620 를 keyserver.ubuntu.com 에 업로드
# gpg --keyserver keyserver.ubuntu.com --send-keys 90F64A666F4E7620
```
