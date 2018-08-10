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

import csv
import sys
import subprocess

print("=-=-=-=-=-=")
print('Clearsigned Public GPG Key CSV Sheet importer for Keysigning Party')
print('Written by Youngbin Han<sukso96100@gmail.com>')
print("=-=-=-=-=-=")

if(len(sys.argv)==6):
    print("""
        사용 방법:
        python3 importer.py (공개키_목록_파일.csv) (핑거프린트 열) (공개키가 있는 열) (키서버) (공개키 보관할 Keyring 이름)
        예: python3 importer.py publickeys.csv 1 2 keyserver.ubuntu.com ksprings.gpg

        GPG 명령행 프로그램이 사전에 설치되어 있어야 본 스크립트를 정상적으로 사용 가능합니다.

        Usage:
        Python3 importer.py (list_of_public_keys.csv) (column_of_fingerprint) (column_of_public_keys) (keyserver) (name_of_keyring_for_storing)
        Example: python3 importer.py publickeys.csv 1 2 keyserver.ubuntu.com ksprings.gpg

        Installation of GPG CLI Program is required to use this script properly.
    """)
else:
    with open(sys.argv[1], newline='') as csvfile:
        keyring_result = subprocess.run(['gpg', '--no-default-keyring','--keyring', str(sys.argv[5]), '--fingerprint'])
        print(keyring_result.stdout)
        print(keyring_result.stderr)
        kspreader = csv.reader(csvfile)
        print("Importing keys to default keyring")
        for index, row in enumerate(kspreader):
            fprint = row[int(sys.argv[2])]
            done = subprocess.run(['gpg', '--keyserver', str(sys.argv[4]) ,'--recv-keys', fprint], encoding='utf8', capture_output=True)
            print(done.stderr)
        for index, row in enumerate(kspreader):
            print("======PROCESSING ITEM {}>=>=>=>".format(index))
            item = row[int(sys.argv[3])]
            done = subprocess.run(['gpg', '--verify'], input=item, encoding='utf8', capture_output=True)
            print(done.stderr)
            signcount = len(done.stderr.split("Signature made"))
            goodcount = len(done.stderr.split("Good signature from"))
            if(signcount>1 and goodcount>1 and signcount==goodcount):
                print('SIGNATURE VERIFIED!')
                if '- -----BEGIN PGP PUBLIC KEY BLOCK-----' in item:
                    sign_and_body = item.split('- -----BEGIN PGP PUBLIC KEY BLOCK-----')[1]
                    body_only = sign_and_body.split('-----BEGIN PGP SIGNATURE-----')[0]
                    publickey = '- -----BEGIN PGP PUBLIC KEY BLOCK-----'.join(['', body_only])
                    # print(publickey)
                    result = subprocess.run(['gpg','--no-default-keyring','--keyring',
                        sys.argv[3], '--import'], input=publickey.replace('- ',''), encoding='utf8')
                    print(result.stdout)
                    print(result.stderr)
            else:
                print('SIGNATURE VERIFICATION FAILED!')
            print(">=>=>=>ITEM {} PROCESSED======".format(index))