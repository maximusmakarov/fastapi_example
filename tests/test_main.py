import pytest

from main import app
from fastapi.testclient import TestClient

client = TestClient(app)

expected_posts_list = [{'date': '2023-03-11T20:48:54.286000',
                        'id': 1,
                        'text': 'Lorem Ipsum - это текст-рыба, часто используемый в печати и '
                                'вэб-дизайне.',
                        'title': 'First post in blog'},
                       {'date': '2023-03-11T21:15:59.337000',
                        'id': 2,
                        'text': 'In this post, I check the work of writing a post to a blog with '
                                'emulation of the processor load for 10 seconds, but in fact I set '
                                'sleep to 10 seconds',
                        'title': 'Second post with try sleep 10 seconds'},
                       {'date': '2023-03-11T21:15:59.337000',
                        'id': 3,
                        'text': 'In this post, I check the work of writing a post to a blog with '
                                'emulation of the processor load for 10 seconds, but in fact I set '
                                'sleep to 10 seconds',
                        'title': 'Second post with try sleep 10 seconds'}]


@pytest.mark.anyio
def test_get_posts_blog():
    response = client.get('/blog')
    assert response.status_code == 200
    assert response.json() == expected_posts_list


def test_post_blog():
    response = client.post('/blog')
    assert response.status_code == 200
