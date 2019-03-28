# -*- coding: utf-8 -*-
"""
Created on Thu Mar 28 14:44:24 2019

@author: nadia
"""

def decrypt_story():
    story=CiphertextMessage(get_story_string())
    return story.decrypt_message()