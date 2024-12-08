import json
import logging
import time

import nltk
from fastapi import FastAPI, HTTPException

from utils import blank_keyword, blank_sentence

app = FastAPI()


@app.get("/")
async def root():
    return "mogomogo Backend!"


@app.get("/probs/{exam_year}/{exam_month}/{item_id}")
async def read_item(exam_year: str, exam_month: str, item_id: str):
    with open(f'data/{exam_year}{exam_month}.json', 'r', encoding='utf-8') as f:
        question_data = json.load(f)
    return question_data.get(item_id)


@app.get("/probs/{exam_year}/{exam_month}/{item_id}/variation")
async def variety_item(exam_year: str, exam_month: str, item_id: str, vr_type: str, word_count: int = 1):
    with open(f'data/{exam_year}{exam_month}.json', 'r', encoding='utf-8') as f:
        question_data = json.load(f)

    question_text = question_data.get(item_id)

    match vr_type:
        case 'words':
            return blank_keyword(question_text, word_count)
        case 'sentences':
            return blank_sentence(question_text)

    raise HTTPException(status_code=400, detail="vr_type is not set!")


# @app.get("/probs/{exam_year}/{exam_month}/{item_id}/variation")
# async def variety_item(exam_year: str, exam_month: str, item_id: str):
#     with open(f'data/{exam_year}{exam_month}.json', 'r', encoding='utf-8') as f:
#         question_data = json.load(f)
#
#     question_text = question_data.get(item_id)
#     return blank_sentence(question_text, is_hint_all=False)


if __name__ == 'main':  # When running server by uvicorn
    fastapi_logger = logging.getLogger('uvicorn')

    fastapi_logger.log(logging.INFO, 'Downloading nltk Data...')
    start_time = time.time()
    nltk.download("all", quiet=True)
    fastapi_logger.log(logging.INFO, f'Done! ({round(time.time() - start_time, 2)}s)')

    fastapi_logger.log(logging.INFO, 'Loaded Server!')

else:
    # When you didn't run by uvicorn (or fastapi-cli), it warns you not to use this method!
    print("========== WARNING ==========\nYou've just run server by unsupported way.\nRun this server by typing `uvicorn main:app --host 0.0.0.0 --reload` instead.")
    # uvicorn.run("main:app", host='0.0.0.0', port=8000, reload=True)
