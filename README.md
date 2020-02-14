# Photo-slideshow
#### Problem statement for the Online Qualication Round of Hash Code 2019

### collaborators chen zhao wong

## Introduction

As the saying goes, "a picture is woh a thousand words." We agree – photos are an
impoant pa of contemporary digital and cultural life. Approximately 2.5 billion
people around the world carry a camera – in the form of a smaphone – in their
pocket every day. We tend to make good use of it, too, taking more photos than ever
(back in 2017, Google Photos announced it was backing up more than 1.2 billion photos
and videos per day).

The rise of digital photography creates an interesting challenge: what should we do
with all of these photos? In this competition problem, we will explore the idea of
composing a slideshow out of a photo collection.

## Task

Given a list of photos and the tags associated with each photo, arrange the photos into
a slideshow that is as interesting as possible (the scoring section below explains what
we mean by “interesting”).

## Problem description

### Photos

A photo is described by a set of tags.

For **example** , a photo with a cat on a beach, during a sunny aernoon could be
tagged with the following tags: [cat, beach, sun].

Each photo's orientation is either horizontal or veical.
**the photo on the le is horizontal, while the photo on the right is veical**

### Slideshow

A slideshow is an ordered list of slides. Each slide contains either:
● a single horizontal photo, or
● two veical photos side-by-side
If the slide contains a single horizontal photo, the tags of the slide are the same as the
tags of the single photo it contains.
For **example** , a slide containing a single horizontal photo with tags [cat, beach, sun],
has tags [cat, beach, sun].
If the slide contains two veical photos, the tags of the slide are all the tags present in
any or both of the two photos it contains.
For **example** , a slide containing two veical photos with tags [sele, smile] for the
rst photo, and tags [garden, sele] for the second photo, has tags [sele, smile,
garden].
Each photo can be used either once or not at all. The slideshow must have **at least** one
slide.