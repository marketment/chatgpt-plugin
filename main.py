from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

app = FastAPI()

# CORS 설정
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"]
)

# 기본 경로
@app.get("/")
def root():
    return {"message": "✅ FastAPI 서버 연결 성공!"}

# 검색 API
@app.get("/search-case")
def search_case(query: str = "손해배상"):
    return {
        "results": [
            {
                "사건명": "손해배상",
                "사건번호": "2022다12345",
                "선고일자": "2023-05-11",
                "판시사항": "이 사건은 계약 위반으로 인한 손해배상 청구 사건이다."
            }
        ]
    }

# 정적 파일 제공 (플러그인 설명 파일 등)
app.mount("/.well-known", StaticFiles(directory=".well-known"), name="well-known")
app.mount("/", StaticFiles(directory=".", html=True), name="static-root")