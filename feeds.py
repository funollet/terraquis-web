from django.contrib.syndication.feeds import Feed
from txts.models import Txt
from django.utils.feedgenerator import Atom1Feed


class TerraquisFeed (Feed):
    '''Generic feed customized for terraquis.net site.'''
    title = "terraquis.net"
    link = "/blog/"
    description = "De terricoles i xarxes."
    feed_type = Atom1Feed

    # We don't want items on feed's top each time it's modified.
    def item_pubdate (self, item):
        return item.pub_date



class BlogEntries (TerraquisFeed):
    '''Feed all blog entries.'''
    def items(self):
        return Txt.public.filter(section__easylink='blog').order_by('-pub_date')[:15]


class OpenKnowledge (TerraquisFeed):
    '''Feed blog entries from selected topics: Open source, CC, open science,...'''
    
    def items(self):
        selected_tags = ['codi-lliure','open-source','net']
        return Txt.public.filter(section__easylink='blog'
            ).filter(tags__value__in=selected_tags).order_by('-pub_date')[:15]
    