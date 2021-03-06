from application import create_app


def test_index():
    '''
    Test the index route.
    '''

    app = create_app()

    with app.test_client() as test_client:
        response = test_client.get('/')
        assert response.status_code == 200
        assert b'The Place to Learn Spanish' in response.data
