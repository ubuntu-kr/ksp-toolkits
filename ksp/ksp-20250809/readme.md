# UbuCon Korea 2025 - OpenPGP 키사이닝 파티

OpenPGP Keysigning Party 에 참여 하고자 하시는 분들은 다음과 같은 사항을 미리 준비하세요.  
도움이 필요 하시거나 문의 사항이 있는 경우, 고민 하지 마시고 [youngbin@ubuntu-kr.org](mailto:youngbin@ubuntu-kr.org) 으로 바로 연락해 주세요.
> 이번 키사이닝 파티는 UbuCon Korea d2025 프로그램의 일부로, 티켓 구입 하시고 오프라인으로 참여 하셔야 참여 가능합니다. [티켓은 여기에서 구입 가능합니다.](https://d2025.ubuntu-kr.org/tickets/)

## PGP, GPG? 키사이닝 파티(Keysigning Party)?
PGP(Pretty Good Privacy) 는 이메일이나 파일 등을 암호화 하거나 전자서명을 할 수 있게 해 주는 공개키 암호화 방식을 사용하는 프로그램 입니다.
GPG(GNU Privacy Guard) 는 PGP 의 OpenPGP 표준의 자유/오픈소스 구현체이며 오늘날 대부분의 리눅스 배포판에서 사용 가능합니다.
PGP(혹은 GPG) 는 이메일과 파일 암호화에도 많이 사용되지만, 오늘날 오픈소스 프로젝트에서 바이너리와 패키지 그리고 패치파일이나 커밋에 서명을 하여 본인이 한 작업물임을 보증되도록 하기 위해 사용 되기도 합니다.

PGP 이외에 우리가 흔히 접하는 SSL/TLS 등 PKI 방식을 사용하는 방식은 인증기관이 있어, 여기서 인증서나 서명 등이 신뢰 할 만한 것인지 확인 해 줍니다. 하지만 PGP는 인증기관의 개념이 없어, PGP키를 만들어 사용하는 각 개인이 인증기관의 역할을 하고, 서로의 신원을 꼼꼼히 확인한 후 서로 키에 서명을 해 주어 인증을 해 주는 형태입니다. 이를 위해서 하는 활동이 OpenPGP Keysigning Party이며, 참여자들이 서로의 신원을 꼼꼼히 확인한 후 서로의 OpenPGP 공개키에 서명을 해 주어OpenPGP 키에 대한  Web of Trust(신뢰 망)을 구축하는 것을 목적으로 하는 행사입니다. 우리가 진행하는 키사이닝 파티 방식은 [Phil Zimmermann과 Len Sassaman의 Hash Based Method Party](http://www.cryptnet.net/fdp/crypto/keysigning_party/en/keysigning_party.html#hash_based)에 기반하여 조금 변형한 형태 입니다.

## 참가자 명단이 나오기 전

> 문서 가이드만으로 이해 및 준비가 어려운 경우, [동영상 가이드](https://www.youtube.com/watch?v=nP5b5bRwZnw)를 시청 하시면서 준비 해 보실 수 있습니다.

- OpenPGP 키를 준비하세요. 아직 강력한 키가 없다면, [**이 문서를 참고하여 새로 준비합니다.**](../../create-gpg-key.md)
    - 키 생성 시 최신 버전의 GPG 명령줄에서 기본으로 사용하는 알고리즘인 `ECC (sign and encrypt) + Curve 25519` 유형을 권장 드립니다.
- 공개키를 키서버에 업로드 합니다. 이번 행사에 참석 하시는 분들은, [keyserver.ubuntu.com](https://keyserver.ubuntu.com) 에 업로드 해주세요.
    - 키서버에 업로드 하는 방법은 [**동일한 문서(공개키 생성 가이드)에 같이 기술되어 있습니다.**](../../create-gpg-key.md)
- 준비된 PGP 키의 핑거프린트 전체(40자리)를 UbuCon Korea 2025 참가 등록 시 `OpenPGP Key Fingerprint ` 입력란에 넣어서 제출 해 주세요.
  - [참가 등록 링크](#)

## 참가자 명단이 나온 후

> 문서 가이드만으로 이해 및 준비가 어려운 경우, [동영상 가이드](https://www.youtube.com/watch?v=oGEcspcn_X0)를 시청 하시면서 준비 해 보실 수 있습니다.

- 명단이 나오면 별도로 공지를 해 드립니다.
- 본 문서의 **파일 목록** 색션에 있는 파일을 모두 다운로드 합니다.
- 각 참가자 목록 파일(`*.txt`)의 SHA256 체크섬을 계산한 후, 각 참가자 목록 파일에 대한 체크섬 파일(`*.txt.sha256`)에 포함된 체크섬과 일치하는지 확인합니다.
    - 다음 명령행을 실행하여 체크섬을 계산합니다: `sha256sum (파일명)`
    - 실행 예시: `sha256sum ksp-20180915-2.txt`
    - 체크섬 일치 확인 실행 예시: `sha256sum ksp-20180915-2.txt | diff ksp-20180915-2.txt.sha256 -` (아무 내용도 뜨지 않아야 함)
- 각 참가자 목록 파일에 대한 서명 파일(`*.txt.asc`)과 각 참가자 목록 파일의 체크섬 파일에 대한 서명 파일(`*.txt.sha256.asc`)의 서명이 올바른지 검증하세요.
    - 서명을 검증하려면 먼저 서명에 쓰인 PGP 키의 공개키를 키서버에서 불러옵니다.
        - 핑거프린트가 `22BE 5648 7B69 D6CD F99D 45AF ACFF 5149 B117 571E` 인 PGP 키로 서명되어 있으며, keyserver.ubuntu.com 에서 불러올 수 있습니다.
        - `gpg --keyserver keyserver.ubuntu.com --recv-keys 22BE56487B69D6CDF99D45AFACFF5149B117571E`
            - [해당 PGP 키 정보 보기](https://keyserver.ubuntu.com/pks/lookup?fingerprint=on&op=index&search=0x22BE56487B69D6CDF99D45AFACFF5149B117571E)
    - Windows(Kleopatra) : Decrypt/Verify... 를 눌러서 검증할 파일을 열어 검증을 진행합니다.
    - MacOS(GPG Suite) : 검증할 파일을 우클릭 한 다음, 서비스 > OpenPGP: Verify Signature of File 를 눌러 진행합니다.
    - Linux: 
        - 다음 명령행을 실행하여 검증합니다.: `gpg --verify < (파일명)`
        - 실행 예시: `gpg --verify < ksp-20180915.txt.sha256.asc`
- 체크섬이 일치하고, 서명이 올바르다면. 이제 참가자 목록 파일을 프린터로 인쇄합니다.
    - 파일 목록에 있는 PDF 파일을 인쇄해도 무방합니다.
    - 인쇄하는 것이 가장 좋지만, 그럴 여건이 안 된다면, 태블릿에서 PDF 파일을 열어 활용하는 방식도 무방합니다. 중요한 것은 체크섬 계산과 서명 검증을 수행을 완료하여 참석하는 것입니다.
- 인쇄한 종이에 본인이 계산한 SHA256 체크섬을 펜으로 직접 옮겨 적습니다.

## 행사 당일
- 각 참가자 목록 파일을 인쇄한 것에 체크섬을 적은 종이와 펜 그리고 본인의 **신분증** 을 지참합니다.
    - 성인의 경우 주민등록증, 운전면허증, 여권 또는 정부기관이 발행한 본인의 사진과 실명이 포함된 신분증을 지참합니다.
    - 청소년의 경우 여권, 청소년증, 학생증 또는 정부기관이 발행한 본인의 사진과 실명이 포함된 신분증을 지참합니다.
    - 외국인의 경우 여권, 외국인 등록증 또는 국제학생증을 지참합니다.
    - 신분증의 이름과 PGP 키에 있는 이름이 동일해야 합니다.
- 키사이닝 세션 시간에 다같이 체크섬을 확인합니다.
- 돌아 다니면서 키사이닝을 교환할 분을 만납니다.
    - 체크섬을 확인합니다. 다같이 확인할 때 확인한 경우 건너뜁니다.
    - 체크섬 확인이 불가능한 경우, 목록에 적힌 핑거프린트와 상대방이 제시하는 핑거프린트를 직접 대조하여 확인합니다.
    - 신분증을 제시하여 서로의 신원을 확인합니다.
    - 충분히 확인된 경우, 종이에서 체크표시 합니다.
    - 만나서 인사 한 김에, 수다 떠는 시간을 조금 가져봅니다.
## 행사 종료 후
[이 문서](../../sign-and-send-key.md) 를 참고해서 신원을 확인한 분들의 공개키에 키사이닝을 한 후 원래 주인분께 공유합니다.  
그리고 본인의 신원을 확인한 분들로부터 키사이닝된 본인의 키를 받아 불러옵니다.

> 참고: 신원을 확인 한 분들이여도, 신뢰하지 않는 사람이라면 꼭 키사이닝을 해 주지 않아도 됩니다. 신원을 확인 했고, 본인이 신뢰하는 분들에게 키사이닝을 해 주는 것이 Web of Trust 를 만들어 가는데 더 도움이 됩니다.

## 파일 목록

- [ksp-uck25-print.pdf](https://raw.githubusercontent.com/ubuntu-kr/ksp-toolkits/master/ksp/ksp-20250809/ksp-uck25-print.pdf)
    - 인쇄용 워크시트 PDF 파일(참가자 공개키 정보, 체크섬 기입란 등 포함)
- [ksp-uck25.txt](https://raw.githubusercontent.com/ubuntu-kr/ksp-toolkits/master/ksp/ksp-20250809/ksp-uck25.txt)
    - 워크시트 파일(참가자 공개키 정보, 체크섬 기입란 등 포함)
- [ksp-uck25.txt.asc](https://raw.githubusercontent.com/ubuntu-kr/ksp-toolkits/master/ksp/ksp-20250809/ksp-uck25.txt.asc)
    - ksp-uck25.txt 파일을 PGP 키 `22BE 5648 7B69 D6CD F99D 45AF ACFF 5149 B117 571E` 로 clearsign 한 파일
- [ksp-uck25.txt.sha256](https://raw.githubusercontent.com/ubuntu-kr/ksp-toolkits/master/ksp/ksp-20250809/ksp-uck25.txt.sha256)
    - ksp-uck25.txt 파일의 SHA256 체크섬을 기록한 파일
- [ksp-uck25.txt.sha256.asc](https://raw.githubusercontent.com/ubuntu-kr/ksp-toolkits/master/ksp/ksp-20250809/ksp-uck25.txt.sha256.asc)
    - ksp-uck25.txt.sha256 파일을 PGP 키 `22BE 5648 7B69 D6CD F99D 45AF ACFF 5149 B117 571E` 로 clearsign 한 파일
