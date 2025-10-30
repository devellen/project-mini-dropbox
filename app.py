import os
import boto3
import mimetypes
from flask import Flask, request, jsonify, render_template
from werkzeug.utils import secure_filename
from botocore.exceptions import ClientError
from dotenv import load_dotenv

# Carregar variáveis do .env
load_dotenv()

AWS_ACCESS_KEY_ID = os.getenv("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = os.getenv("AWS_SECRET_ACCESS_KEY")
AWS_SESSION_TOKEN = os.getenv("AWS_SESSION_TOKEN")
AWS_REGION = os.getenv("AWS_REGION")
S3_BUCKET = os.getenv("S3_BUCKET")

# Configuração do S3
s3 = boto3.client(
    "s3",
    aws_access_key_id=AWS_ACCESS_KEY_ID,
    aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
    aws_session_token=AWS_SESSION_TOKEN,
    region_name=AWS_REGION
)

app = Flask(__name__)

# Página principal
@app.route("/")
def index():
    return render_template("index.html")

# Upload
@app.route("/upload", methods=["POST"])
def upload_file():
    file = request.files.get("file")
    if not file:
        return jsonify({"error": "Nenhum arquivo enviado"}), 400

    filename = secure_filename(file.filename)
    content_type, _ = mimetypes.guess_type(filename)
    if not content_type:
        content_type = "application/octet-stream"

    try:
        s3.upload_fileobj(
            Fileobj=file,
            Bucket=S3_BUCKET,
            Key=filename,
            ExtraArgs={"ContentType": content_type}
        )
        return jsonify({"message": "Upload concluído!", "filename": filename})
    except ClientError as e:
        return jsonify({"error": str(e)}), 500

# Listagem
@app.route("/list", methods=["GET"])
def list_files():
    try:
        resp = s3.list_objects_v2(Bucket=S3_BUCKET)
        files = []
        for obj in resp.get("Contents", []):
            key = obj["Key"]
            try:
                head = s3.head_object(Bucket=S3_BUCKET, Key=key)
                ct = head.get("ContentType")
            except Exception:
                ct = None
            files.append({
                "key": key,
                "size": obj["Size"],
                "last_modified": obj["LastModified"].isoformat(),
                "content_type": ct
            })
        return jsonify({"files": files})
    except ClientError as e:
        return jsonify({"error": str(e)}), 500

# Download
@app.route("/download", methods=["GET"])
def download_file():
    key = request.args.get("key")
    if not key:
        return jsonify({"error": "Parâmetro 'key' obrigatório"}), 400
    try:
        url = s3.generate_presigned_url(
            ClientMethod="get_object",
            Params={
                "Bucket": S3_BUCKET,
                "Key": key,
                "ResponseContentDisposition": f"attachment; filename={key}"
            },
            ExpiresIn=300
        )
        return jsonify({"url": url})
    except ClientError as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True, port=5000)
