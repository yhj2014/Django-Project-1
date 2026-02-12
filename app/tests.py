from django.test import TestCase, Client
from django.urls import reverse
from .form import TestForm

class TestFormTestCase(TestCase):
    """测试表单验证功能"""
    
    def test_valid_form(self):
        """测试有效的表单数据"""
        form_data = {'name': '张三', 'age': 25}
        form = TestForm(data=form_data)
        self.assertTrue(form.is_valid())
    
    def test_invalid_name(self):
        """测试无效的姓名（长度超过限制）"""
        form_data = {'name': '张三李四王五赵六七八九十', 'age': 25}  # 超过10个字符
        form = TestForm(data=form_data)
        self.assertFalse(form.is_valid())
    
    def test_invalid_age(self):
        """测试无效的年龄（超出范围）"""
        # 测试年龄过小
        form_data = {'name': '张三', 'age': 0}
        form = TestForm(data=form_data)
        self.assertFalse(form.is_valid())
        
        # 测试年龄过大
        form_data = {'name': '张三', 'age': 201}
        form = TestForm(data=form_data)
        self.assertFalse(form.is_valid())

class TestViewTestCase(TestCase):
    """测试视图函数功能"""
    
    def setUp(self):
        """设置测试客户端"""
        self.client = Client()
    
    def test_index_get(self):
        """测试GET请求访问index视图"""
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')
    
    def test_index_post_valid(self):
        """测试POST请求提交有效数据"""
        form_data = {'name': '张三', 'age': 25}
        response = self.client.post(reverse('index'), data=form_data)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'app/result.html')
        self.assertContains(response, '张三')
        self.assertContains(response, '25')
    
    def test_index_post_invalid(self):
        """测试POST请求提交无效数据"""
        form_data = {'name': '张三李四王五赵六七八九十', 'age': 25}  # 超过10个字符的姓名
        response = self.client.post(reverse('index'), data=form_data)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

class TestUrlTestCase(TestCase):
    """测试URL配置"""
    
    def test_index_url(self):
        """测试index URL是否正确映射"""
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)