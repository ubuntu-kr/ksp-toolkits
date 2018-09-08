"""
The MIT License (MIT)
Copyright 2018-Present Youngbin Han<sukso96100@gmail.com>

Permission is hereby granted, free of charge, to any person
obtaining a copy of this software and associated documentation files (the "Software"),
to deal in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software,
and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included
in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED,
INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""

import subprocess, sys

print("=-=-=-=-=-=")
print('Worksheet generator for GPG Keysigning Party')
print('Written by Youngbin Han<sukso96100@gmail.com>')
print("=-=-=-=-=-=")

print("워크시트 제목을 입력하세요.")
print("Write title of the worksheet.")

howto = """
참여자 목록 / List of participants

본 파일로 하셔야 할 일:
1. 본 파일을 인새하세요.
2. 본 파일의 SHA256 체크섬을 계산하세요.
3. 본 파일과 같이 제공된 체크섬 파일에 있는 값과 비교합니다.
4. 계산한 체크섬을 인쇄물의 체크섬 기록란에 씁니다.
5. 인쇄물, 신분증, 필기구를 지참하여 행사에 참석합니다.

다른 키사이닝 파티 참여자를 만나셨을 떄 하셔야 할 일:
1. 서로 계산해 온 체크섬이 일치하는지 확인합니다.
2. 목록에서의 서로의 번호를 확인하고, 목록에 있는 서로의 핑거프린트에 문제가 없는지 확인합니다.
3. 목록상의 신원 정보와 상대방의 신원정보가 일치하는지 서로 유효한 신분증(정부기관 발급 신분증, 여권 등)을 제시하여 확인합니다.
4. 신원을 충분히 확인 했다면, 인쇄물의 해당 항목에 체크표시 하여
해당 항목의 GPG 핑거프린트와 신원을 확인했음을 표시합니다.

Here's what you have to do with this file:
1. Print this file to paper.
2. Compute this file's SHA256 checksum
3. fill in the hash values on the printout.
4. Bring the printout, a pen, and proof of identity to the keysigning.

For each participant:
1. Compare the hash you computed with the other participant.
2. Ask if the other participant's gpg fingerprint on the hardcopy is correct.
3. Verify each other's identity by checking valid ID(Government issued ID, Passport, etc.).
4. If you are satisfied with the identification, mark on your hardcopy that
the other participant's gpg fingerprint is correct and has been identified.

SHA256 Checksum / SHA256 체크섬 :

____________________________________________________________________ [ ]
"""

if(len(sys.argv)!=5):
    print("""
        사용 방법:
        python3 printer.py (공개키 보관된 Keyring 이름) (행사 제목(워크시트 제목)) (부제목) (행사 준비자 정보) > (파일명).txt
        예: python3 printer.py ksprings.gpg "우분투한국커뮤니티 9월 서울지역 세미나" "GPG Keysigning Party" "한영빈(Youngbin Han)<sukso96100@gmail.com>" > list.txt

        GPG 명령행 프로그램이 사전에 설치되어 있어야 본 스크립트를 정상적으로 사용 가능합니다.

        Usage:
        Python3 printer.py (name_of_keyring_to_print) (event_name(worksheet_name)) (subtitle) (prepared_by)
        Example: python3 printer.py ksprings.gpg "우분투한국커뮤니티 9월 서울지역 세미나" "GPG Keysigning Party" "한영빈(Youngbin Han)<sukso96100@gmail.com>" > list.txt

        Installation of GPG CLI Program is required to use this script properly.
    """)
else:
    userInput = "{}\n{}\n행사 준비: {}\n\n".format(str(sys.argv[2]), str(sys.argv[3]), str(sys.argv[4]))
    userInput += howto
    keyring_result = subprocess.run(['gpg', '--no-default-keyring','--keyring', str(sys.argv[1]), '--list-keys'], capture_output=True, text=True)
    print(keyring_result.stdout)
    body = keyring_result.stdout.split('----------------------------------')[1]
    splited = body.split('pub ')
    for index, item in enumerate(splited):
        # print("=====================
        userInput += "\n#{} [ ] 핑거프린트 확인(Fingerprint OK) [ ] 신원 확인(ID OK)\npub{}".format(index, item)
    print(userInput)
