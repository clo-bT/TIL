entry_record = ['이싸피', '박장고', '조실습', '이싸피', '조실습', '오디비', '임온실', '조실습', '조실습', '이싸피', '안도둑', '임온실', '최이썬', '오디비', '안도둑', '염자바', '박장고', '조실습',
                '최이썬', '조실습', '염자바', '박장고', '임온실', '임온실', '이싸피', '임온실', '오디비', '조실습', '염자바', '임온실', '박장고', '최이썬', '안도둑', '염자바', '임온실', '박장고', '이싸피', '안도둑',
                '임온실', '오디비', '최이썬', '안도둑', '이싸피', '오디비', '안도둑', '이싸피', '박장고', '박장고', '안도둑', '안도둑', '안도둑', '염자바', '최이썬', '오디비', '오디비', '최이썬', '이싸피', '임온실', '안도둑']

exit_record = ['최이썬', '조실습', '이싸피', '안도둑', '임온실', '안도둑', '이싸피', '오디비', '염자바', '박장고', '최이썬', '이싸피', '염자바', '염자바', '박장고', '임온실', '이싸피',
               '박장고', '안도둑', '염자바', '이싸피', '조실습', '조실습', '임온실', '박장고', '이싸피', '조실습', '박장고', '오디비', '안도둑', '조실습', '임온실', '안도둑', '안도둑', '임온실', '조실습', '최이썬', '안도둑', '임온실',
               '염자바', '이싸피', '임온실', '안도둑', '오디비', '안도둑', '오디비', '임온실', '염자바', '임온실', '박장고', '조실습', '이싸피', '최이썬', '최이썬', '오디비', '오디비', '염자바', '오디비', '안도둑', '박장고']

from collections import Counter

cmc = Counter(entry_record).most_common(3) # 입장기록 많은 세명. type= list안에 tuple
print('입장 기록 많은 Top3')
for c in cmc:
    print(f'{c[0]} {c[1]}회')
# print(f'입장 기록 많은 Top3\n{cmc[0][0]} {cmc[0][1]}회\n{cmc[1][0]} {cmc[1][1]}회\n{cmc[2][0]} {cmc[2][1]}회')
entry_ext = dict(Counter(entry_record) - Counter(exit_record)) #dict
ext_entry = dict(Counter(exit_record) - Counter(entry_record))

print('\n출입 기록이 수상한 사람')
e = list(entry_ext.keys())
v = list(entry_ext.values())
k = list(ext_entry.keys())
b = list(ext_entry.values())
print(f'{e[0]}은 입장 기록이 {v[0]}회 더 많아 수상합니다')
print(f'{k[0]}은 퇴장 기록이 {b[0]}회 더 많아 수상합니다')