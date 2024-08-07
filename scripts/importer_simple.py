"""
The MIT License (MIT)
Copyright 2024-Present Youngbin Han<sukso96100@gmail.com>

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

import argparse
import csv
import subprocess

parser = argparse.ArgumentParser(description='OpenPGP Key Fingerprint CSV Sheet importer for Keysigning Party - by Youngbin Han<sukso96100@gmail.com>')
parser.add_argument("-k", "--pubkeys-csv-path", type=str, help='OpenPGP 공개키가 저장된 CSV 파일 경로')
parser.add_argument("-f", "--fingerprint-row", type=int, help='OpenPGP 핑거프린트가 있는 열')
parser.add_argument("-s", "--keyserver", type=str, help='OpenPGP 키서버 URL', default='keyserver.ubuntu.com')
parser.add_argument("-r", "--keyring-name", type=str, help='불러온 OpenPGP키를 보관할 키링 이름')
args = parser.parse_args()

with open(args.pubkeys_csv_path, newline='') as csvfile:
    keyring_result = subprocess.run(['gpg', '--no-default-keyring', '--keyring', args.keyring_name, '--fingerprint'])
    print(keyring_result.stdout)
    print(keyring_result.stderr)
    kspreader = csv.reader(csvfile)
    print("Importing keys to the keyring")
    # print(f"Total {len(list(kspreader))} items to process...")
    for index, row in enumerate(kspreader):
        print(f"======PROCESSING ITEM {index}>=>=>=>")
        fprint = row[int(args.fingerprint_row)]
        done = subprocess.run(['gpg', '--no-default-keyring', '--keyring', args.keyring_name, '--keyserver', args.keyserver ,'--recv-keys', fprint], encoding='utf8', capture_output=True)
        print(done.stderr)
        
        print(f">=>=>=>ITEM {index} PROCESSED======")