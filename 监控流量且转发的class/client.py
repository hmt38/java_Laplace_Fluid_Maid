from flask import Flask, request

app = Flask(__name__)

@app.route('/<path:path>', methods=['POST', 'GET'])
def handle_request(path):
    # 获取请求方法
    method = request.method

    # 获取请求头
    headers = request.headers

    # 获取请求体
    body = request.get_data(as_text=True)

    # 输出请求信息到控制台
    print(f"Method: {method}")
    print(f"Path: /{path}")
    print("Headers:")
    for header, value in headers.items():
        print(f"{header}: {value}")
    print(f"Body: {body}")
    print("***********************")
    return "OK"

if __name__ == '__main__':
    app.run(port=3307)