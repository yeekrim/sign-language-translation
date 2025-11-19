from transformers import T5ForConditionalGeneration, T5TokenizerFast

MODEL_PATH = r"/Users/kyungrim/Library/CloudStorage/GoogleDrive-20221999@edu.hanbat.ac.kr/내 드라이브/2025캡스톤프로젝트/my_finetuned_t5_model"

try:
    tokenizer = T5TokenizerFast.from_pretrained(MODEL_PATH)
    model = T5ForConditionalGeneration.from_pretrained(MODEL_PATH)
    print("✅ 모델과 토크나이저를 성공적으로 불러왔습니다.")
except Exception as e:
    print(f"❌ 모델 로딩 중 오류 발생: {e}")
    print("👉 1~3단계를 다시 확인해보세요. 특히 이전 폴더 삭제와 재학습이 완료되었는지 확인이 필요합니다.")
    exit()

prompt = "i, love, you"
print(f"📝 테스트 입력: '{prompt}'")

# 토큰화 및 문장 생성
inputs = tokenizer(prompt, return_tensors="pt")
outputs = model.generate(
    inputs.input_ids,
    max_length=64,
    num_beams=5,
    early_stopping=True
)

# 결과 확인
result = tokenizer.decode(outputs[0], skip_special_tokens=True)
print(f"✅ 모델 생성 문장: {result}")