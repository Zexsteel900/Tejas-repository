{
    "nbformat": 4,
    "nbformat_minor": 0,
    "metadata": {
        "colab": {
            "provenance": [],
            "mount_file_id": "1087tp0y1ZrTyrOLJJ-HRddnOxhv-zJMo",
            "authorship_tag": "ABX9TyPwrkGxCt9eCB7SUDujLQ20",
        },
        "kernelspec": {"name": "python3", "display_name": "Python 3"},
        "language_info": {"name": "python"},
    },
    "cells": [
        {
            "cell_type": "code",
            "execution_count": null,
            "metadata": {
                "colab": {"base_uri": "https://localhost:8080/"},
                "id": "AEnFVa77yQ7d",
                "executionInfo": {
                    "status": "ok",
                    "timestamp": 1694629975414,
                    "user_tz": -330,
                    "elapsed": 5344,
                    "user": {
                        "displayName": "MANSI PRASAD",
                        "userId": "08205378784200194542",
                    },
                },
                "outputId": "379928d6-6dcc-48dd-9ab7-fd23768b0b53",
            },
            "outputs": [
                {
                    "output_type": "stream",
                    "name": "stdout",
                    "text": [
                        "Collecting flask-ngrok\n",
                        "  Downloading flask_ngrok-0.0.25-py3-none-any.whl (3.1 kB)\n",
                        "Requirement already satisfied: Flask>=0.8 in /usr/local/lib/python3.10/dist-packages (from flask-ngrok) (2.2.5)\n",
                        "Requirement already satisfied: requests in /usr/local/lib/python3.10/dist-packages (from flask-ngrok) (2.31.0)\n",
                        "Requirement already satisfied: Werkzeug>=2.2.2 in /usr/local/lib/python3.10/dist-packages (from Flask>=0.8->flask-ngrok) (2.3.7)\n",
                        "Requirement already satisfied: Jinja2>=3.0 in /usr/local/lib/python3.10/dist-packages (from Flask>=0.8->flask-ngrok) (3.1.2)\n",
                        "Requirement already satisfied: itsdangerous>=2.0 in /usr/local/lib/python3.10/dist-packages (from Flask>=0.8->flask-ngrok) (2.1.2)\n",
                        "Requirement already satisfied: click>=8.0 in /usr/local/lib/python3.10/dist-packages (from Flask>=0.8->flask-ngrok) (8.1.7)\n",
                        "Requirement already satisfied: charset-normalizer<4,>=2 in /usr/local/lib/python3.10/dist-packages (from requests->flask-ngrok) (3.2.0)\n",
                        "Requirement already satisfied: idna<4,>=2.5 in /usr/local/lib/python3.10/dist-packages (from requests->flask-ngrok) (3.4)\n",
                        "Requirement already satisfied: urllib3<3,>=1.21.1 in /usr/local/lib/python3.10/dist-packages (from requests->flask-ngrok) (2.0.4)\n",
                        "Requirement already satisfied: certifi>=2017.4.17 in /usr/local/lib/python3.10/dist-packages (from requests->flask-ngrok) (2023.7.22)\n",
                        "Requirement already satisfied: MarkupSafe>=2.0 in /usr/local/lib/python3.10/dist-packages (from Jinja2>=3.0->Flask>=0.8->flask-ngrok) (2.1.3)\n",
                        "Installing collected packages: flask-ngrok\n",
                        "Successfully installed flask-ngrok-0.0.25\n",
                    ],
                }
            ],
            "source": ["pip install flask-ngrok"],
        },
        {
            "cell_type": "code",
            "source": ["cd /content/drive/MyDrive/SIH"],
            "metadata": {
                "colab": {"base_uri": "https://localhost:8080/"},
                "id": "N9PkSvId1t2l",
                "executionInfo": {
                    "status": "ok",
                    "timestamp": 1694696739192,
                    "user_tz": -330,
                    "elapsed": 629,
                    "user": {
                        "displayName": "MANSI PRASAD",
                        "userId": "08205378784200194542",
                    },
                },
                "outputId": "1b34cb8b-b25b-48bf-9601-2cfdc49475d1",
            },
            "execution_count": 2,
            "outputs": [
                {
                    "output_type": "stream",
                    "name": "stdout",
                    "text": ["/content/drive/MyDrive/SIH\n"],
                }
            ],
        },
        {
            "cell_type": "code",
            "source": [
                "from flask import Flask, render_template, request, jsonify\n",
                "import numpy as np\n",
                "import cv2\n",
                "from keras.models import load_model",
            ],
            "metadata": {
                "id": "8u_0nWd12SBH",
                "executionInfo": {
                    "status": "ok",
                    "timestamp": 1694696387006,
                    "user_tz": -330,
                    "elapsed": 5629,
                    "user": {
                        "displayName": "MANSI PRASAD",
                        "userId": "08205378784200194542",
                    },
                },
            },
            "execution_count": 1,
            "outputs": [],
        },
        {
            "cell_type": "markdown",
            "source": ["Loading Model"],
            "metadata": {"id": "A91qfetVz2Bi"},
        },
        {
            "cell_type": "code",
            "source": ["model = load_model('model.pkl')"],
            "metadata": {"id": "yKic_3mw3UjT"},
            "execution_count": null,
            "outputs": [],
        },
        {
            "cell_type": "markdown",
            "source": ["**Flask Application**"],
            "metadata": {"id": "H_OKE_Ts2ycr"},
        },
        {
            "cell_type": "code",
            "source": [
                "def predict(image):\n",
                "  image= cv2.resize(image, (224, 224))\n",
                "  image = np.array(image)/255.0\n",
                "  image = np.expand_dims(image, axis=0)\n",
            ],
            "metadata": {
                "colab": {"base_uri": "https://localhost:8080/", "height": 210},
                "id": "mPk0BgUW3Xc8",
                "executionInfo": {
                    "status": "error",
                    "timestamp": 1694630883296,
                    "user_tz": -330,
                    "elapsed": 484,
                    "user": {
                        "displayName": "MANSI PRASAD",
                        "userId": "08205378784200194542",
                    },
                },
                "outputId": "83fecefb-4d59-4ca8-a14a-997681dbd187",
            },
            "execution_count": null,
            "outputs": [
                {
                    "output_type": "error",
                    "ename": "FileNotFoundError",
                    "evalue": "ignored",
                    "traceback": [
                        "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
                        "\u001b[0;31mFileNotFoundError\u001b[0m                         Traceback (most recent call last)",
                        "\u001b[0;32m<ipython-input-6-594a8f2b1dec>\u001b[0m in \u001b[0;36m<cell line: 3>\u001b[0;34m()\u001b[0m\n\u001b[1;32m      1\u001b[0m \u001b[0mapp\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mFlask\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0m__name__\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      2\u001b[0m \u001b[0mrun_with_ngrok\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mapp\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m----> 3\u001b[0;31m \u001b[0mmodel\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mpickle\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mload\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mopen\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m'Skin_disease.pkl'\u001b[0m \u001b[0;34m,\u001b[0m \u001b[0;34m'rb'\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m",
                        "\u001b[0;31mFileNotFoundError\u001b[0m: [Errno 2] No such file or directory: 'Skin_disease.pkl'",
                    ],
                }
            ],
        },
        {
            "cell_type": "markdown",
            "source": ["Make a Prediction"],
            "metadata": {"id": "12mhYGwT0kF4"},
        },
        {
            "cell_type": "code",
            "source": ["prediction = model.predict(image)"],
            "metadata": {"id": "otH-uKlv_WJx"},
            "execution_count": null,
            "outputs": [],
        },
        {
            "cell_type": "markdown",
            "source": ["Return Prediction"],
            "metadata": {"id": "fcxTrldM0nQL"},
        },
        {
            "cell_type": "code",
            "source": ["return prediction[0][0]"],
            "metadata": {"id": "ecfJb_14_qfx"},
            "execution_count": null,
            "outputs": [],
        },
        {
            "cell_type": "code",
            "source": ["app = Flask(__name__)"],
            "metadata": {"id": "p580xwrRA5Pp"},
            "execution_count": null,
            "outputs": [],
        },
        {
            "cell_type": "code",
            "source": ["@app.route('/predict', methods=[POST])"],
            "metadata": {"id": "pbt548sQ09KL"},
            "execution_count": null,
            "outputs": [],
        },
        {
            "cell_type": "code",
            "source": [
                "def predict_image():\n",
                "  image_file=request.files['images']\n",
                "  image = cv2.imread(images, cv2.IMREAD_COLOR)\n",
            ],
            "metadata": {"id": "BnNVTIRh1JIC"},
            "execution_count": null,
            "outputs": [],
        },
        {
            "cell_type": "code",
            "source": ["prediction = predict(image)\n"],
            "metadata": {"id": "oyMKCTM_13TJ"},
            "execution_count": null,
            "outputs": [],
        },
        {
            "cell_type": "code",
            "source": [
                'prediction_string = "Cancer Detected" if prediction>0.5 else "Cancer not detected"'
            ],
            "metadata": {"id": "x-D7aqQx1-Kl"},
            "execution_count": null,
            "outputs": [],
        },
        {
            "cell_type": "code",
            "source": ["return jsonify({'prediction': prediction_string})"],
            "metadata": {"id": "Sp-IVe2t2OEr"},
            "execution_count": null,
            "outputs": [],
        },
        {
            "cell_type": "markdown",
            "source": ["FLASK APPLLICATION"],
            "metadata": {"id": "sYeaKVic2ZmW"},
        },
        {
            "cell_type": "code",
            "source": ["if __name__=='__main__':\n", "   app.run(debug=True)"],
            "metadata": {"id": "oTq6dwM22dF7"},
            "execution_count": null,
            "outputs": [],
        },
        {
            "cell_type": "code",
            "source": [],
            "metadata": {"id": "q1zRsyVl2X3u"},
            "execution_count": null,
            "outputs": [],
        },
    ],
}
