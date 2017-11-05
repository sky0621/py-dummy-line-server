from bottle import route, run, template, post, request

if __name__ == "__main__":
    # 設定ファイル読み込み
    run(host='localhost', port=5050, reloader=True)

@post("/v2/bot/message/reply")
def reply():
    contentType = request.headers.get('Content-Type')
    print(contentType)
    authorization = request.headers.get('Authorization')
    print(authorization)
    replyToken = request.forms.get('replyToken')
    print(replyToken)
    messages = request.forms.get('messages')
    print(messages)
    return template("{}")