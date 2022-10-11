shop = {'kim99': 12000, 'lee66': 11000, 'han55': 3000, 'hong77': 5000, 'hwang33': 18000}
num = 1

for k in shop: # k = key
    print(f'{num}. 아이디: {k}, 마일리지: {shop[k]}점')
    num += 1

score = []

for k in shop:
    score.append(shop[k])
    
result = max(score) # result에 최댓값 저장

# 최댓값을 가진 회원 추출
for k in shop:
    if shop[k] == result:
        result_key = k
        
print('%s님의 %d점이 가장 높은 점수입니다.' % (result_key, result))