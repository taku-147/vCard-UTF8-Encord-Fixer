import os
import quopri
import sys
import re



# QUOTED-PRINTABLE形式のデコード関数
def decode_quoted_printable(text):
    return quopri.decodestring(text).decode('utf-8')


# vCardの修正処理
def fix_vcard_file(input_path):
    output_path = os.path.splitext(input_path)[0] + "_fix.vcf"

    with open(input_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    fixed_lines = []
    temp_line = ""

    for line in lines:
        line = line.rstrip()
        if line.endswith('='):
            temp_line += line[:-1]
        else:
            temp_line += line
            if 'ENCODING=QUOTED-PRINTABLE' in temp_line:
                try:
                    key, value = temp_line.split(':', 1)
                    decoded_value = decode_quoted_printable(value.strip())
                    fixed_lines.append(f"{key}:{decoded_value}")
                except Exception as e:
                    print(f"Error decoding line: {temp_line} | Reason: {e}")
                    fixed_lines.append(temp_line)
            elif temp_line.startswith("VERSION:2.1"):
                fixed_lines.append("VERSION:3.0")
            else:
                fixed_lines.append(temp_line)
            temp_line = ""

    # EMAIL;OTHER: の置き換え
    fixed_lines = [re.sub(r"EMAIL;([^:]+):", r"EMAIL;TYPE=\1;TYPE=pref;TYPE=INTERNET:", line) for line in fixed_lines]

    with open(output_path, 'w', encoding='utf-8') as output_file:
        output_file.writelines("\n".join(fixed_lines) + "\n")

    print(f"修正済みのvCardファイルが保存されました: {output_path}")

# 実行
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python vcard_utf8_encord_fix.py <input_file_path>")
    else:
        input_file_path = sys.argv[1]
        fix_vcard_file(input_file_path)