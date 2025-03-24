from modules.postprocessor import merge_and_rank_results
from modules.rag import stepback_rerank, stepback_rankgpt
from modules import text2sql_pipeline

query = "서울 도봉구에 사는 34세 청년 남자에게 맞는 정책을 추천해줘"

# 두 방식으로 결과 뽑기
rerank_results = stepback_rerank.run(query)       # 점수 포함된 리스트
rankgpt_results = stepback_rankgpt.run(query)
text2sql_results = text2sql_pipeline.run(query)

# 병합 및 Top-15 추출
top_15 = merge_and_rank_results(rerank_results, rankgpt_results, text2sql_results,top_k=15)

top3_fields = list({item["서비스분야"] for item in top_15[:3] if "서비스분야" in item}) 
# 출력부분에 위에 서비스분야 해시태그처럼 다는거

print("🟦 Top3 분야 태그:", top3_fields)

for i, item in enumerate(top_15, 1):
    print(f"{i}. {item['서비스명']}")
    print(f"서비스 ID: {item['정책ID']}")
    print(item['지원내용'])
    print()