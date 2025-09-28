import unittest
from unittest.mock import patch
import github_user_data_retrival

class TestGitHubApi(unittest.TestCase):
    def test_get_github_user_data(self):
        with patch('github_user_data_retrival.requests.get') as mock_get:
            mock_get.side_effect = [
                type('Response', (), {
                    'status_code': 200,
                    'json': lambda: [{'name': 'test-repo'}]
                }),
                type('Response', (), {
                    'status_code': 200,
                    'json': lambda: [{'sha': 'abc123'}]  # One commit
                })
            ]

            result = github_user_data_retrival.get_github_user_data_retrival('testuser')
            expected = [{'repo': 'test-repo', 'commits': 1}]  # Expect 1 commit
            self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()