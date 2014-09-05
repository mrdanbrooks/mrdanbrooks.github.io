---
layout: post
title: Making tags work with Github pages
published: true
---

Based on this tutorial by [minddust](http://www.minddust.com/post/tags-and-categories-on-github-pages/), I was able to get tags to semi-automatically fill out tag pages. You still have to make a page for each tag, but at least it is automatically populated with posts now. 

I created the file ``_includes/gen_tags_content.html``.

```html
{% raw %}
{% if post.tags.size > 0 %}
    {% capture tags_content %}Posted with {% if post.tags.size == 1 %}<i class="fa fa-tag"></i>{% else %}<i class="fa fa-tags"></i>{% endif %}: {% endcapture %}
    {% for post_tag in post.tags %}
        {% for data_tag in site.data.tags %}
            {% if data_tag.slug == post_tag %}
                {% assign tag = data_tag %}
            {% endif %}
        {% endfor %}
        {% if tag %}
            {% capture tags_content_temp %}{{ tags_content }}<a href="/tags/{{ tag.slug }}/">{{ tag.name }}</a>{% if forloop.last == false %}, {% endif %}{% endcapture %}
            {% assign tags_content = tags_content_temp %}
            {% assign tag  = false  %}
        {% else %}
            {% capture tags_content_temp %}{{ tags_content }}<a href="/tags/{{ post_tag }}/">{{ post_tag }}</a>{% if forloop.last == false %}, {% endif %}{% endcapture %}
            {% assign tags_content = tags_content_temp %}
        {% endif %}
    {% endfor %}
{% else %}
    {% assign tags_content = '' %}
{% endif %}
{% endraw %}
```

This is pretty similar to minddust's script, but also allows for you to use tags that are not in ``_data/tags.yml`` (see below). This file gets included anywhere you want to generate the list of tags for a post, but that is all it does. Then, in your ``_layouts/post.html`` you need to add the following lines.

```html+django
{% raw %}
{% assign post = page %}
{% include gen_tags_content.html %}
...
{{ tags_content}}
%{ endraw %}
```

The first two lines should go near the top of the file, while the last line goes where you want the tags to print out.
I found the first line to be necessary because the script in ``_include/gen_tags_content.html`` references post, but the data is actually in page. 

On your **post entry**, you can now add tags in the header. 

```yaml
---
layout: post
title: How To Use Tags And Categories On GitHub Pages Without Plugins
category: programming
tags: [github, github-pages, jekyll]
---
```

At this point, tags are printing out, but the links dont work. For every tag you want to have the link work, you need to do the following steps:

Enable relative permalinks in your ``_config.yml`` by adding the following line. This is needed to make your pages end up in a url that corresponds to the directories they are in.

```yaml
relative_permalinks: true
```

Next we need to make a layout template for our tag lists. Put the following in a file at ``_layouts/blog_by_tag.html``

```
{% raw %}
--- 
layout: default
---

<h1>Articles related to {{ page.tag }}</h1>
<div>
    {% if site.tags[page.tag] %}
        {% for post in site.tags[page.tag] %}
            <a href="{{ post.url }}/">{{ post.title }}</a>
        {% endfor %}
    {% else %}
        <p>There are no posts for this tag.</p>
    {% endif %}
</div>
{% endraw %}
```


Finally, for each tag you want a page for (in other words, a working link), create a page at ``/tags/mytagname.md`` that looks like this.

```yaml
---
layout: blog_by_tag
tag: mytagname
permalink: mytagname/
---
```

This will render a page at the corresponding url that uses the blog_by_tag layout seeded to create a list using the supplied tag.


Now, if you want to have pretty tags, you need to create a ``_data/tags.yml``. This will allow you to have things like spaces in tag names. Add entries to it like so

```yaml
- slug: github-pages
  name: GitHub Pages
```
