from flask import Flask, jsonify
import requests

app = Flask(__name__)

@app.route('/prices', methods=['GET'])
def get_crypto_prices():
    # Use CoinDesk API to get Bitcoin price (you can change it to any crypto API)
    response = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
    if response.status_code == 200:
        data = response.json()
        return jsonify({
            'Bitcoin Price': data['bpi']['USD']['rate'],
            'Currency': 'USD'
        })
    else:
        return jsonify({'error': 'Could not fetch data'}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
