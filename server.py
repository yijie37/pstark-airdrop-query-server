import json
from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
import os

router = FastAPI()

origins = [
    # "http://localhost",
    # "http://localhost:3000",
    # "http://192.168.0.101:3000",
    "*"
    # 添加其他允许的域
]

router.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_methods=["*"],  # 允许所有的请求方式
    allow_headers=["*"],  # 允许所有的请求头
)

allocation = {}
# 读取文件内容到内存
for i in range(5):
    f = f'./pstark_airdrop{i}.json'
    with open(f, 'r', encoding='utf-8') as fr:
        obj = json.load(fr)
        for k, v in obj.items():
            allocation[k] = int(v)

@router.get("/check_allocation")
async def check_allocation(addr: str):
    return allocation.get(addr, 0)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app='server', host="0.0.0.0", port=9955, reload=True)
