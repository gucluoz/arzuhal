from django.test import TestCase

from web.models import Subject

class SubjectTestCase(TestCase):
  def setUp(self):
    Subject.objects.create(name='testSubject1', containerdirectory='testDir1')
    Subject.objects.create(name='testSubject2', containerdirectory='testDir2')

  def test_subject_exists(self):
    testObject = Subject.objects.get(name='testSubject1')
    self.assertEqual(testObject.containerdirectory, 'testDir1')