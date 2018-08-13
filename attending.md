# 참가자용 도움말

## 행사 참가 전
행사 공지사항을 먼저 확인하고, 공지사항에 따라 사전에 준비할 사항을 미리 준비합니다.

### GPG 키 준비
- GPG 키가 없는 경우 새로 생성합니다.
    - 행사마다 차이가 있으나, Web of Trust 를 확보하기 위한 행사인 만큼, 강력한 키 기준을 요구 또는 권장하는 경우도 있습니다.
        - 일부 오픈소스 프로젝트는 공식 구성원이 되려면 GPG 키가 필요한데, 이때 강력한 키 기준을 요구 하기도 합니다.
    - 이미 쓰던 키 인데, 기준을 만족하지 못하거나 너무 오래된 키긴 경우, 키를 수정하거나 필요하면 새로 만듭니다.
    - 2018년 기준, 아래와 같은 기준을 권장합니다. 최근 나오는 gpg 도구는 아래 기준을 거의 다 만족하는 키를 생성해 줍니다.
        - 키 길이는 최소 3072(3072 또는 4096)
        - 키 유형은 RSA and RSA 유형
        - 해싱 알고리즘은 SHA 256 이상(SHA 256 또는 SHA 512) - SHA1 은 보안 취약점이 있으므로 사용하지 않습니다.
        - 약 2년 안에 만료
        - PGP v4 버전 이상
        - Comment 필드 사용 자제
        - 이름과 이메일은 본인의 실명과 실제 많이 쓰는 이메일 주소로
    - GPG 키 생성 방법은 [이 문서](create-gpg-key.md) 를 참고하세요.

### GPG 키 제출

공개키를 먼저 키서버에 업로드 합니다. 업로드할 키서버는 매 행사마다 다릅니다.

명령행을 이용하여, 제출한 GPG 키의 공개키를 내보냅니다.
```
gpg --armor --export-options export-clean,export-minimal --export <키ID_또는_핑거프린트_공백없이> > <원하는_파일명>
# 예시 : gpg --armor --export-options export-clean,export-minimal --export DC2742A8 > publickey
```
GUI 앱의 경우, 다음과 같은 방법으로 내보내기 합니다.
- Linux(Seahorse)
    - 키 항목을 선택 후, 편집 > 복사
    - 텍스트 편집기를 연 다음, 붙여넣기 하고 해당 내용을 새 텍스트 파일로 저장.
- MacOS(GPG Suite)
    - 키 항목을 선택 후, 편집 > 복사
    - 텍스트 편집기를 연 다음, 붙여넣기 하고 해당 내용을 새 텍스트 파일로 저장.
- Windows(Kleopatra)
    - 키 항목을 선택 후, `Export`를 눌러서 내보냅니다.

그 다음, 공개키 파일을 서명(Clearsign)합니다.
```
gpg --local-user <키ID_또는_핑거프린트_공백없이> --clearsign <공개키_파일>
# 예시 : gpg --local-user DC2742A8 --clearsign publickey

```

생성된 `<공개키_파일명>.asc` 파일을 연 다음 파일 내용을 이메일 등의 방법으로 제출합니다.

아래는 여러분이 제출해야 하는 서명된(Clearsign 된) 공개키 블록의 예시 입니다.

```
-----BEGIN PGP SIGNED MESSAGE-----
Hash: SHA512

- -----BEGIN PGP PUBLIC KEY BLOCK-----

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
hmgzj1WGp0edUyk=
=lO6x
- -----END PGP PUBLIC KEY BLOCK-----
-----BEGIN PGP SIGNATURE-----

iQIzBAEBCgAdFiEE2MgQOxbFbjS1b5pCMLcp9xIThZkFAltuJlIACgkQMLcp9xIT
hZlikw//aJkLYdAjqkWuIX/GkMWHJT7zFBb2pvaSGY80Ik4jZSny1G0HkhJdr+MR
DP9+ejq0Qcu8jetKHJ/7tiu35j85894G+wt4Pa2zp0Oin9bNAqO0f/JuV36ueRbp
UozRlk+VccnpZ1YtFPztDnfOWf7QA5kGcbXdDwEU+eQu10E3w6oj/oe/N1wcE1aS
cWMexuLZOAoIBwciJRVRzYR15FZgdmIPl8VwOdCx5e7YjU0L+phQ2aNFxme+rDve
ncv0lPMWsIu7tVwmdmrwChXTXCf44HQynfwDLo4VXR42Ij9zAcqBkkdth4uVGbLn
nlinyXKzDVNU5W8TlMruDG+hzgrNDIgLWT0ASBHNIdZxIGfR3fGQeXo6tCD6LFZE
IL+rwHa7yGPqEaF79r3yDjkvaZAEVA5vGUixNRqdPaVEThmlKJiM2qz1o1gOtZmh
SNaMT9wcPL4+UMc2qy8seTbj7T1Mfk3deDLSlhTSHEPs9+Isxy0Jlzf0rDJuVe6P
7zegzaIpIGrDyrPxdi1D7kVjxZHiBS3ksvo5hQKL4SVDuHp53BRurOsF0cshkSui
p8ZtJn+GnKjMcxaUY/jbZjIfaRccjQDVSvFP+NrZNLjFL1GGW/lBiz/1aBzybnad
W1BrLSwcq7JgBiE+dRj8YQ28Sk31RJNSTF4+GNtdVtxYmxCoU0s=
=3Jjk
-----END PGP SIGNATURE-----

```
