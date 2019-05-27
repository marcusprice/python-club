from django.test import TestCase
from .models import Meeting, MeetingMinutes, Resource, Event
from .forms import MeetingForm

# Create your tests here.
class MeetingTest(TestCase):
    def test_string(self):
        type=Meeting(meetingtitle="Functions Meeting")
        self.assertEqual(str(type), type.meetingtitle)

    def test_table(self):
        self.assertEqual(str(Meeting._meta.db_table), 'meeting')


class MeetingMinutesTest(TestCase):
    def test_string(self):
        type=MeetingMinutes(minutestext="Lorum Ipsum")
        self.assertEqual(str(type), type.minutestext)

    def test_table(self):
        self.assertEqual(str(MeetingMinutes._meta.db_table), 'meetingminutes')

class ResourceTest(TestCase):
    def test_string(self):
        type=Resource(resourcename="Laptop")
        self.assertEqual(str(type), type.resourcename)

    def test_table(self):
        self.assertEqual(str(Resource._meta.db_table), 'resource')

class EventTest(TestCase):
    def test_string(self):
        type=Event(eventtitle="Python and Pizza")
        self.assertEqual(str(type), type.eventtitle)

    def test_table(self):
        self.assertEqual(str(Event._meta.db_table), 'event')


#Form tests
class Meeting_Form_Test(TestCase):
    def test_meetingform_is_valid(self):
        form=MeetingForm(data={'meetingtitle': "title1", 'meetingdate' : "2019-05-31", 'location': "scc", 'agenda': "some agenda"})
        self.assertTrue(form.is_valid())


    def test_meetingform_empty(self):
        form=MeetingForm(data={'meetingtitle': ""})
        self.assertFalse(form.is_valid())
