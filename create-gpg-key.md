# GPG 키 생성하기
* 이 문서는 GPG 키를 생성하는 방법을 적은 가이드 문서입니다.

# 패키지 설치하기
## Ubuntu 16.04
gpg 명령어 사용을 위한 패키지 설치
```
sudo apt install gnupg
```

## Ubuntu 18.04
gpg 명령어 사용을 위한 패키지 설치
```
sudo apt install gnupg
```

## Debian, 혹은 다른 Debian 계열의 운영체제
gpg 명령어 사용을 위한 패키지 설치
```
sudo apt install gnupg
```
or
```
sudo apt-get install gnupg
```

## Mac OS X 
gpg 명령어 사용을 위한 패키지 설치
Homebrew 를 사용하여 설치합니다.
```
brew install gpg
```

# 키 생성 하기

- 먼저, `~/.gnupg/gpg.conf` 파일에, 아래와 같은 내용을 가장 마지막 줄에 추가합니다.
    - 키 생성시 키의 해싱 알고리즘 기본값을 정하는 설정입니다.
```
personal-digest-preferences SHA512
cert-digest-algo SHA512
default-preference-list SHA512 SHA384 SHA256 SHA224 AES256 AES192 AES CAST5 ZLIB BZIP2 ZIP Uncompressed
```

- 아래 명령으로, 키 생성을 시작합니다.
```bash
gpg --full-generate-key
# 또는 gpg --full-gen-key
# GPG 2.1 이전 버전인 경우(Ubuntu 16.04 이전) gpg --gen-key
```

- 키 유형은 RSA and RSA 로 합니다.
```
Please select what kind of key you want:
   (1) RSA and RSA (default)
   (2) DSA and Elgamal
   (3) DSA (sign only)
   (4) RSA (sign only)
Your selection? 1
```

- 키 길이는 최소 3072 이상으로 합니다. 4096을 권장합니다.
```
RSA keys may be between 1024 and 4096 bits long.
What keysize do you want? (2048) 4096
```

- 키 유효기간을 정합니다. 약 2년 안으로 하는 것을 권장합니다.
```
Please specify how long the key should be valid.
         0 = key does not expire
      <n>  = key expires in n days
      <n>w = key expires in n weeks
      <n>m = key expires in n months
      <n>y = key expires in n years
Key is valid for? (0) 2y
```

- 개인 신원을 입력합니다. 이름은 실명을 한글 또는 영문으로, 이메일은 자주 쓰는 것으로 사용합니다. 커멘트는 비워두는것이 좋습니다.
```
You need a user ID to identify your key; the software constructs the user ID
from the Real Name, Comment and Email Address in this form:
    "Heinrich Heine (Der Dichter) <heinrichh@duesseldorf.de>"

Real name: Test User
Email address: test@example.org
Comment: 
```

- 입력한 신원 정보 일치 여부를 확인합니다. 이후, 키가 생성 과정이 시작되는데, 랜담 바이트가 필요합니다. 웹 브라우징 등으로 랜덤 바이트 생성을 하면서 기다립니다.
```
You selected this USER-ID:
    "Test User <test@example.org>"

Change (N)ame, (C)omment, (E)mail or (O)kay/(Q)uit? o
You need a Passphrase to protect your secret key.

passphrase not correctly repeated; try again.
We need to generate a lot of random bytes. It is a good idea to perform
some other action (type on the keyboard, move the mouse, utilize the
disks) during the prime generation; this gives the random number
generator a better chance to gain enough entropy.
..........+++++
.................................+++++
```

-> 엔트로 제너레이션 : https://serverfault.com/questions/214605/gpg-does-not-have-enough-entropy

공개키를 키서버에 업로드 하려면 아래와 같이 실햅합니다.
> 키ID 는 GPG 키 핑거프린트의 마지막 8자리 입니다.
```bash
gpg --keyserver <키서버 주소> --send-keys <키ID_또는_핑거프린트>
```

## GUI 앱 사용

### Windows (gpg3win - Kleopatra)
- https://www.gpg4win.org/index.html 에서 프로그램을 받아 설치합니다.
- Kelopatra 프로그램을 사용하겠습니다. 프로그램을 켜고, `New Key Pair` 버튼을 누릅니다.   
![](images/gpg-windows-1.png)

- 본인의 신원 정보를 입력합니다. 실명과 자주 쓰는 이메일 주소를 입력합니다. 그리고 추가 설정을 위해, `Advanced Settings...` 을 누릅니다.   
![](images/gpg-windows-2.png)

- 키 유형과 길이, 만료일을 설정해 줍니다. 키 길이는 3072 이상으로 합니다. 4096을 권장합니다.   
![](images/gpg-windows-3.png)

- 키 정보를 확인한 후, `Create` 를 눌러 키 생성을 합니다.   
![](images/gpg-windows-4.png)

- 사용할 키 비밀번호를 입력합니다. 그리고 잠시 기다립니다.   
![](images/gpg-windows-5.png)

- 키가 생성되었습니다.   
![](images/gpg-windows-6.png)

> 2018년 7월 기준, gpg4win 의 Kleopatra 는 키의 기본 해싱 알고리즘을 SHA256 으로 하여 키를 생성합니다. 참고하시기 바랍니다.

- 키를 키서버에 업로드 하려면, 먼저 `설정`>`Kleopatra 설정` 으로 이동합니다.
- `OpenPGP Keyserver` 란에 키서버 주소를 입력한 뒤, 적용하고 확인을 누릅니다.
- 키서버에 올릴 항목을 우클릭 한 다음, `Publish on Server` 를 눌러 커서버에 업로드 합니다.

### Ubuntu, Debian (Seahorse)
- 먼저, `~/.gnupg/gpg.conf` 파일에, 아래와 같은 내용을 가장 마지막 줄에 추가합니다.
    - 키 생성시 키의 해싱 알고리즘 기본값을 정하는 설정입니다.
```
personal-digest-preferences SHA512
cert-digest-algo SHA512
default-preference-list SHA512 SHA384 SHA256 SHA224 AES256 AES192 AES CAST5 ZLIB BZIP2 ZIP Uncompressed
```

- `+` 버튼을 눌러 키 생성을 시작합니다.   
![](images/linux-seahorse-1.png)

- `PGP 키` 를 선택합니다.   
![](images/linux-seahorse-2.png)

- 신원 정보를 입력합니다. 이름은 실명을, 이메일은 자주 사용하는 것으로 합니다.
- 고급 키 옵션에서, 암호화는 RSA, 키 강도를 3072이상(4096을 권장합니디.), 만료일을 약 2년 안으로 합니다.   
![](images/linux-seahorse-3.png)

- 암호를 지정합니다.   
![](images/linux-seahorse-4.png)

- 잠시 기다리면, 키가 사진처럼 생성 됩니다.   
![](images/linux-seahorse-5.png)

- 키서버에 업로드 하려면 다음을 따릅니다.
    - 편집 > 기본설정 으로 이동합니다.
    - "키를 찾는 방법(F)" 에 키서버 목록이 있습니다. 원하는 키서버가 없다면, "추가" 버튼을 이용하여 추가합니다.
    - 키서버를 새로 추가한 경우 설정 창을 닫았다가 다시 엽니다.
    - "키를 공개할 곳(P)" 에서 키를 업로드한 키서버를 선택합니다. 그리고 설정창을 닫습니다.
    - 업로드할 키 항목을 선택하고, 원격 > 키 동기화 및 공개(S)... 를 이용하여 업로드 합니다.
### MacOS
- 먼저, `~/.gnupg/gpg.conf` 파일에, 아래와 같은 내용을 가장 마지막 줄에 추가합니다.
    - 키 생성시 키의 해싱 알고리즘 기본값을 정하는 설정입니다.
```
personal-digest-preferences SHA512
cert-digest-algo SHA512
default-preference-list SHA512 SHA384 SHA256 SHA224 AES256 AES192 AES CAST5 ZLIB BZIP2 ZIP Uncompressed
```

- GPG Suite 를 https://gpgtools.org/ 에서 내려받아 설치합니다. 
- `New` 를 눌러 키를 생성합니다.
- 이름, 이메일 주소, 비밀번호, 비밀번호 확인 을 순서대로 입력합니다.
- 고급옵션을 열고, 키 길이를 최소 3072(4096 이상을 권장합니다.)로 설정합니다.
- `Generate Key` 를 눌러 키를 생성합니다.
![](images/macos-1.png)

- 키서버에 올리려면,
    - GPG Keychain 앱에 포커스를 둔 뒤, 메뉴바에서 GPG Keychain > 설정... 으로 들어갑니다.
    - 키서버 탭에서 키서버 주소를 변경합니다.
    - 설정 창을 닫고. 키서버에 보낼 항목을 우클릭 한 뒤, `Send Public Key to Key Server` 를 눌러 키서버에 올립니다.
