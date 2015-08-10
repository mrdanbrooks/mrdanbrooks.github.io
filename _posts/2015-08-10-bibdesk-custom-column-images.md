---
layout: post
title: Adding Custom Table Column Images to BibDesk
tags: osx
category: random
year: 2015
month: 08
day: 10
published: true
summary: Explains how to add custom images to the table in BibDesk
---
By default, the main table shows the name of the field in the headers of the column, and for the `Local-Url` and `Url` fields it shows a small file icon and a `@` symbol respecitively. 
Sometimes you might want more columns to show images in the header to identify the column, for example if you have added custom Local File or Remote URL fields in the Custom Types and Fields.

You can add your own custom image to use in the table column header.
Let's say you have added a custom Remote URL field called `Citeseerurl`, and you want the header for the corresponding column to show an image which you have put at the location `/Users/YourName/Library/Application Support/BibDesk/CiteSeer.png`.
For Bibdesk to use this image, quit BibDesk and enter the following command in Terminal (exclude the outer double quotes):

```
defaults write -app BibDesk BDSKTableHeaderImages -dict-add Citeseerurl "/Users/YourName/Library/Application Support/BibDesk/CiteSeer.png"
```

You can add as many field name/image path pairs as you like inside the braces.

Similarly, you can also replace the default field name by a title of your own choice, such as the `@` symbol for the `Url` field.
For this, follow the same procedure as for images, but use the key ``BDSKTableHeaderTitles`` instead, and write the title to appear in the header instead of the image path. 

----------------------------------------
I've copied the text above from the BibDesk Help pages explaining how to add icons to the table in BibDesk.
Here is the [Link to the BibDesk help page](http://bibdesk.sourceforge.net/manual/BibDeskHelp_73.html).
