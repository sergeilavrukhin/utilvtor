from rest_framework import serializers

from .models import WasteCodes


class WasteCodesSerializer(serializers.ModelSerializer):
    code_space = serializers.SerializerMethodField(help_text='Код с пробелами')

    class Meta:
        model = WasteCodes
        fields = ('code', 'name', 'code_space')

    @staticmethod
    def get_code_space(el):
        code_space = (
            f"{el.code[0]} {el.code[1:3]} {el.code[3:6]} "
            f"{el.code[6:8]} {el.code[8:10]} {el.code[10]}"
        )
        return code_space
