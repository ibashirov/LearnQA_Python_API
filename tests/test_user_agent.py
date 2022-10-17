import requests
import pytest


class TestUserAgent:
    agent_data = [
        ({"User-Agent":"Mozilla/5.0 (Linux; U; Android 4.0.2; en-us; Galaxy Nexus Build/ICL53F) AppleWebKit/534.30 "
          "(KHTML, like Gecko) Version/4.0 Mobile Safari/534.30",
          "expected_platform": "Mobile",
          "expected_browser": "No",
          "expected_device":"Android"
          }),
        ({"User-Agent":"Mozilla/5.0 (iPad; CPU OS 13_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) "
          "CriOS/91.0.4472.77 Mobile/15E148 Safari/604.1",
          "expected_platform": "Mobile",
          "expected_browser": "Chrome",
          "expected_device": "iOS"
          }),
        ({"User-Agent":"Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)",
          "expected_platform": "Googlebot",
          "expected_browser": "Unknown",
          "expected_device": "Unknown"
          }),
        ({"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
          "Chrome/91.0.4472.77 Safari/537.36 Edg/91.0.100.0",
          "expected_platform": "Web",
          "expected_browser": "Chrome",
          "expected_device": "No"
          }),
        ({"User-Agent":"Mozilla/5.0 (iPad; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, "
                       "like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1",
          "expected_platform": "Mobile",
          "expected_browser": "No",
          "expected_device": "iPhone"
          })
    ]
    @pytest.mark.parametrize('agent_data', agent_data)
    def test_user_agent(self, agent_data):
        user_agent = agent_data["User-Agent"]
        expected_platform = agent_data["expected_platform"]
        expected_browser = agent_data["expected_browser"]
        expected_device = agent_data["expected_device"]

        response = requests.get("https://playground.learnqa.ru/ajax/api/user_agent_check", headers={'User-Agent': user_agent}).json()
        actual_platform = response['platform']
        actual_browser = response['browser']
        actual_device = response['device']

        assert expected_platform == actual_platform, f"User Agent: {user_agent}. Not correct platform. Expected: {expected_platform}. Actual: {actual_platform}"
        assert expected_browser == actual_browser, f"User Agent: {user_agent}. Not correct browser. Expected: {expected_browser}. Actual: {actual_browser}"
        assert expected_device == actual_device, f"User Agent: {user_agent}. Not correct device. Expected: {expected_device}. Actual: {actual_device}"