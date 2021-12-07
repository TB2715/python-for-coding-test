s = input()

a_ascii = ord('a')
z_ascii = ord('z')

alphabet = ['-1' for _ in range(z_ascii-a_ascii+1)]

for sidx, s_char in enumerate(s):
    if alphabet[ord(s_char)-a_ascii] == '-1':
        alphabet[ord(s_char)-a_ascii] = str(sidx)

print(' '.join(alphabet))