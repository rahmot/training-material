""" Unit tests for the functions imported into app.py

to run enter "pytest test_app.py" in terminal"""

from select_story import select_story
from select_story import story_list


def test_select_story_result_received():
    selected_story_title, selected_story = select_story()
    assert selected_story_title in set(story_list.keys())
    assert selected_story in set(story_list.values())

def test_select_story_story_and_author_aligned():
    selected_story_title, selected_story = select_story()
    stories = list(story_list.values())
    titles = list(story_list.keys())
    assert len(stories) == len(titles)
    assert titles.index(selected_story_title) == stories.index(selected_story)