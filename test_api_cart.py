import requests

endpoint = 'https://v8ru.ru/cart'
endpoint_1 = 'https://v8ru.ru/?page=addToBasket'
endpoint_2 = 'https://api.github.com'
endpoint_3 = 'https://openweathermap.org'


def test_get_cart_1():
    response = requests.get(endpoint)
    print('\nResponse: ', response.headers)
    key = 'Date'
    assert key in response.headers

def test_post_cart_1():
    payload = {
        'checkExistingArticleInCart': True,
        'number': 'cuk1919',
        'brand': 'MANN-FILTER',
        'dataSetKey': 'zxXJyUXQAJ3NSKlusCWAjK1TyW7cMAz9lUBnZyBvzdi3JF0wQNu06DEtDNmip0Rky9Ay6SDIv5eSMx6nxyIXWnyiycdH6olJEFLhCKxOs2TxmkH8YXVWnJHd2GtWMxYQhQcwx2YyuhUtKnRHVvOEWT9NCsE0nZZwirWdwcmhHgn46XmRFcHm22jbYIsu2ixafhE%2Fabzm56AcopUzPgfl0clX16t8c2gx%2F1wRlRUpOxnsqCNWb8tic7VdoDMwrW%2BnO%2B9W3g%2BhICIpz8rNFYnkJykcNA6HUCLjWX7Jy0ueXvCyLqq6rF5L0UjohVfuDSV51W3yP%2FqIg0C1jLNMGMpGonUGW%2B%2B0oW7f5VXBac6dNwbG7tiY0DSSUOm%2FoI7yJGxvJlaPXqmEPQLufxPKN3lZJeyglQ9qkXpoP4yiVfBF2IevfmiBivVCWSBSUmJQTKhv83yovLPzLj4xWkDpO7eTEUcHw8vxEYSJFOjc%2Bt0g9mBZff8r1LrxS3alOxGy24%2FE8Jb2w4YFeSbaWkv7iVJMt8vW9OIBIgl76uiA43dPD2EnX5K3Rozyru%2FBvD8P%2B1qpz1RHnRhog3ukhq6Nw05BAJ%2F%2FAkVoGxc%3D',
        'distributorRouteId': '11428843'
        }
    response = requests.post(endpoint_1, json=payload)
    assert response.status_code == 200




