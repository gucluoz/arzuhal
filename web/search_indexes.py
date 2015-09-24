import datetime
from haystack import indexes
from web.models import Petition


class PetitionIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)

    def get_model(self):
        return Petition

    def index_queryset(self, using=None):
        return self.get_model().objects.all()