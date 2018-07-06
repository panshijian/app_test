import pytest,allure

class Test_001:
    @allure.step(title = "这是第一个测试")
    @pytest.allure.severity(pytest.allure.severity_level.BLOCKER)


    def test_01(self):
        @allure.attach("描述","我是测试步骤1")



        # print("test_01---->")
        assert 0
    @allure.step(title = "这是第二条测试用例")
    @pytest.allure.severity(pytest.allure.severity_level.CRITICAL)
    def test_02(self):
        # print("test_02----->")
        @allure.attach("描述","这是第二条测试")
        assert 1