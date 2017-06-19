from django_filters.rest_framework import NumberFilter, FilterSet, MultipleChoiceFilter, CharFilter, \
    ModelMultipleChoiceFilter
from rest_framework import serializers

from aroma.models import Aroma, Brand, Note, Group, Nose, CategoryNotes
from activity.models import Activity
from core.settings import GENDER_CHOICES


class SearchFilter(FilterSet):
    min_year = NumberFilter(name="year", lookup_expr='gte')
    max_year = NumberFilter(name="year", lookup_expr='lte')
    title = CharFilter(name="title", lookup_expr='contains')
    gender = MultipleChoiceFilter(choices=GENDER_CHOICES,
                                  method=lambda queryset, name, value: queryset.filter(gender__in=value))
    notes = ModelMultipleChoiceFilter(queryset=Note.objects.all(), conjoined=True)
    groups = ModelMultipleChoiceFilter(name="groups", queryset=Group.objects.all(), conjoined=True)
    noses = ModelMultipleChoiceFilter(name="noses", queryset=Nose.objects.all(), conjoined=True)

    class Meta:
        model = Aroma
        fields = ('gender', 'min_year', 'max_year', 'title', 'brand', 'notes', 'notes', 'groups', 'noses')


class AromaCommonSerializer(serializers.ModelSerializer):
    favorite = serializers.SerializerMethodField('_favorite')
    like = serializers.SerializerMethodField('_like')

    def _favorite(self, obj):
        return obj.get_mark_by_type(Activity.FAVORITE, self.context['request'].user)

    def _like(self, obj):
        return obj.get_mark_by_type(Activity.LIKE, self.context['request'].user)


class AromaListSerializer(AromaCommonSerializer):
    groups = serializers.SlugRelatedField(read_only=True, many=True, slug_field='title')
    brand = serializers.SlugRelatedField(read_only=True, slug_field='title')

    class Meta:
        model = Aroma
        fields = ('id', 'title', 'year', 'brand', 'pic', 'groups', 'favorite', 'like', 'url')
        extra_kwargs = {
            'url': {'lookup_field': 'slug'}
        }


class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = '__all__'


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = ('id', 'title', 'logo')


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ('id', 'title')


class NoseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Nose
        fields = ('id', 'name')


class AromaDetailSerializer(AromaCommonSerializer):
    top_notes = serializers.SerializerMethodField()
    middle_notes = serializers.SerializerMethodField()
    base_notes = serializers.SerializerMethodField()
    general_notes = serializers.SerializerMethodField()
    noses = NoseSerializer(read_only=True, many=True)
    gender_label = serializers.SerializerMethodField()
    brand = BrandSerializer(read_only=True)
    groups = GroupSerializer(read_only=True, many=True)

    @staticmethod
    def get_gender_label(obj):
        return obj.get_gender_display()

    @staticmethod
    def get_top_notes(obj):
        notes = obj.notes.filter(categorynotes__category=CategoryNotes.TOP_NOTES).all()
        return NoteSerializer(notes, many=True, read_only=True).data

    @staticmethod
    def get_middle_notes(obj):
        notes = obj.notes.filter(categorynotes__category=CategoryNotes.MIDDLE_NOTES).all()
        return NoteSerializer(notes, many=True, read_only=True).data

    @staticmethod
    def get_base_notes(obj):
        notes = obj.notes.filter(categorynotes__category=CategoryNotes.BASE_NOTES).all()
        return NoteSerializer(notes, many=True, read_only=True).data

    @staticmethod
    def get_general_notes(obj):
        notes = obj.notes.filter(categorynotes__category=CategoryNotes.GENERAL_NOTES).all()
        return NoteSerializer(notes, many=True, read_only=True).data

    class Meta:
        model = Aroma
        fields = ('id', 'title', 'year', 'brand', 'pic', 'groups', 'gender', 'gender_label', 'noses', 'description',
                  'top_notes', 'middle_notes', 'base_notes', 'general_notes', 'favorite', 'like')
