# Photo-slideshow
#### Problem statement for the Online Qualication Round of Hash Code 2019


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


## Input data set

### File format

Each input data set is provided in a plain text le containing exclusively ASCII
characters with lines terminated with a single '\n' character (UNIX- style line endings).
The rst line of the data set contains a single integer _N_ ( _1 ≤ N ≤ 10_^5 ) — the number of
photos in the collection.
This is followed by _N_ lines, where line _i_ contains a description of the photo with ID _i_
(0 ≤  _i_  <  _N_ ). The description of photo _i_ contains the following data, separated by a single
space:
● A single character ‘H’ if the photo is horizontal, or ‘V’ if it is veical.
● An integer _M_ i (1 ≤  _M_ i  ≤ 100) — the number of tags for that photo.
● _M i_ text strings — the tags for photo _i_. Each tag consists only of lowercase ASCII

### leers and digits, between 1 and 10 characters in total.

### Example

```
cat, beach, sun sele, smile garden, sele garden, cat
Input file Description
4 
H 3 cat beach sun
V 2 selfie smile
V 2 garden selfie
H 2 garden cat
The collection has 4 photos
Photo 0 is horizontal and has tags [cat, beach, sun]
Photo 1 is vertical and has tags [selfie, smile]
Photo 2 is vertical and has tags [garden, selfie]
Photo 3 is horizontal and has tags [garden, cat]
```

## Submissions

### File format

The output le must sta with a single integer _S_ ( _1 ≤ S ≤ N _ )— the number of slides in the
slideshow. This must be followed by _S_ lines describing the individual slides. Each line
should contain either:
● A single integer – ID of the single horizontal photo in the slide.
● Two integers separated by a single space – IDs of the two veical photos in the
slide in any order.
Each photo can be used only one time or not at all.

### Example

```
slide S 0 slide S 1 slide S 2 
Submission file Description
3 
0 
3 
1 
The slideshow has 3 slides
First slide contains photo 
Second slide contains photo 
Third slide contains photos 1 and 
```

### Scoring

The slideshow is scored based on how interesting the transitions between each pair of
subsequent (neighboring) slides are. We want the transitions to have something in
common to preserve continuity (the two slides should not be totally dierent), but we
also want them to be dierent enough to keep the audience interested. The similarity
of two veical photos on a single slide is not taken into account for the scoring
function. This means that two photos can, but don't have to, have tags in common.
For two subsequent slides _S i_ and _S i+1_ , the interest factor is the minimum (the smallest
number of the three) of:
● the number of common tags between _S i_ and _S i+_
● the number of tags in _S i_ but not in _S i+_
● the number of tags in _S i+1_ but not in _S i_.
For **example** , for the slide transition from S 1 to S 2 , we know that the tags are [garden,
cat] for S 1 , and [sele, smile, garden] for S 2 :
● The number of common tags is 1 → [garden]
● The number of tags in S 1 , but not is S 2 is 1 → [cat]
● The number of tags in S 2 , but not in S 1 , is 2 → [sele and smile]
The interest factor is the minimum of these numbers, so it is 1.
For a slideshow of S slides, the score will be equal to the sum of interest factors of
each transition of two neighboring slides. A slideshow with only one slide has a score
of zero.


For **example** , with the input and the submission les above, the slideshow has 3
slides, hence it has 2 transitions:
1st transition, from slide S 0 (photo 0) to slide S 1 (photo 3)
● 1 common tag between photos 0 and 3 → [cat]
● 2 tags in photo 0 and not in photo 3 → [beach, sun]
● 1 tag in photo 3 and not in photo 0 → [garden]
Interest factor = min(1, 2, 1) = 1
Second transition, from slide S 1 (photo 3) to slide S 2 (photos 1, 2) has interest factor 1
(see example above).
Therefore, the score of this submission is 1 + 1 = 2.
**Note that there are multiple data sets representing separate instances of the problem. The nal
score for your team will be the sum of your best scores on the individual data sets.**



[base64str]:data:image/jpg;base64,/9j/4AAQSkZJRgABAQIAHAAcAAD/2wBDAAMCAgICAgMCAgIDAwMDBAYEBAQEBAgGBgUGCQgKCgkICQkKDA8MCgsOCwkJDRENDg8QEBEQCgwSExIQEw8QEBD/wAALCAC/AckBAREA/8QAHQABAAMAAgMBAAAAAAAAAAAAAAcICQYKAgQFA//EAEsQAAEDAwMCAwMGCgYHCQAAAAEAAgMEBQYHCBEJEhMhMRRBURUiOGFxdSMyQmJzdoGCs7QWFzM2N7UkNVJydLGyGTRTWJGWocHT/9oACAEBAAA/ANU0RERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERRxuG1xxzbhpHetYsstVyuVrsbqVs1NbhGah/j1EcDe0SOa3ydK0nkjyB+xVw0O6qui2vGq2PaR41p9m1Bc8jqH09PU10VIII3NifIS8smc7jhhHkD5kK6yIiIiIiKoW5XqW6R7YdUqnSjMcGy+6XKlo6esdUWyOlMBZM3uaAZJmu5A9fJS5tb3NYhuv04qdTMJsV4tNvprrNaHQXVsTZjLHHFIXDw3vb2kTNA8+eQfJTCiIiIiIiIiIq87uN62nuzuPFZM8xfIryMsNaKX5IZA7wvZvA7+/xZGevtDeOOfQ88eXPobS99um27+85DZMExLJbPLjlLBVVD7syna2Rsr3NaGeFK88gtPPPCsqiIiIiIiIiIiIiIiIqm9VD6DWoX6az/5rSrJrpyfTX0s+86j+TnXYXRERERERYT9XT6Zl3+4rX/CKvP0Zfom3b9dbh/K0aviiIiIiIiIiIsr+uZ/3bRb9JkP/ACt6430Pv7/6p/c9u/jSrXRERERERERERERERERVN6qH0GtQv01n/wA1pVjls41WxDQ3cRjW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ERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERf/2Q==
![avatar][base64str]