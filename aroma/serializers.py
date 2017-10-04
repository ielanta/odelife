from functools import reduce
from operator import and_
from django.conf import settings
from django.db.models import Q
from django_filters.rest_framework import NumberFilter, FilterSet, MultipleChoiceFilter, CharFilter, \
    ModelMultipleChoiceFilter
from rest_framework import serializers

from activity.models import Activity
from activity.serializers import CommentSerializer
from collaboration.models import Interaction
from aroma.models import Aroma, Brand, Note, Group, Nose, CategoryNotes
from tag.models import Tag


class SearchFilter(FilterSet):
    min_year = NumberFilter(name="year", lookup_expr='gte')
    max_year = NumberFilter(name="year", lookup_expr='lte')
    title = CharFilter(name="title", method=lambda queryset, name, value: queryset
                       .filter(reduce(and_, [Q(title__icontains=s) for s in value.split()])))
    gender = MultipleChoiceFilter(choices=settings.GENDER_CHOICES,
                                  method=lambda queryset, name, value: queryset.filter(gender__in=value))
    in_notes = ModelMultipleChoiceFilter(name="notes", queryset=Note.objects.all(), conjoined=True)
    ex_notes = ModelMultipleChoiceFilter(name="notes", queryset=Note.objects.all(), conjoined=True, exclude=True)
    groups = ModelMultipleChoiceFilter(name="groups", queryset=Group.objects.all(), conjoined=True)
    noses = ModelMultipleChoiceFilter(name="noses", queryset=Nose.objects.all(), conjoined=True)
    tags = ModelMultipleChoiceFilter(name="taggeditem__tag", queryset=Tag.objects.all(), conjoined=True)

    class Meta:
        model = Aroma
        fields = ('gender', 'min_year', 'max_year', 'title', 'brand', 'in_notes', 'notes', 'groups', 'noses', 'tags')


class AromaCommonSerializer(serializers.ModelSerializer):
    favorite = serializers.SerializerMethodField('_favorite')
    like = serializers.SerializerMethodField('_like')
    tags = serializers.SerializerMethodField()

    def _favorite(self, obj):
        return obj.get_mark_by_type(Activity.FAVORITE, self.context['request'].user)

    def _like(self, obj):
        return obj.get_mark_by_type(Activity.LIKE, self.context['request'].user)

    @staticmethod
    def get_tags(obj):
        return obj.get_tags()


class AromaListSerializer(AromaCommonSerializer):
    groups = serializers.SlugRelatedField(read_only=True, many=True, slug_field='title')
    brand = serializers.SlugRelatedField(read_only=True, slug_field='title')

    class Meta:
        model = Aroma
        fields = ('id', 'title', 'year', 'brand', 'pic', 'groups', 'favorite', 'like', 'url', 'comments_counter', 'tags')
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
        fields = ('id', 'title', 'logo', 'ru_trans')


class InteractionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Interaction
        fields = ('link', 'price')


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
    comments = serializers.SerializerMethodField()
    # interaction = serializers.SerializerMethodField()

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

    @staticmethod
    def get_comments(obj):
        comments = obj.comment_set.filter(is_approved=True).order_by('-created_at').all()
        return CommentSerializer(comments, many=True, read_only=True).data

    # @staticmethod
    # def get_interaction(obj):
    #     return obj.interaction_set.first()

    class Meta:
        model = Aroma
        fields = ('id', 'title', 'year', 'brand', 'pic', 'groups', 'gender', 'gender_label', 'noses', 'description',
                  'top_notes', 'middle_notes', 'base_notes', 'general_notes', 'favorite', 'like', 'comments', 'tags',
                  'video', 'ru_trans')
