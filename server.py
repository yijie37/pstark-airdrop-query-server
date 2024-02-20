import json
from fastapi import FastAPI, File, UploadFile
import os

router = FastAPI()

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
    uvicorn.run(app='server', host="0.0.0.0", port=9966, reload=True)
