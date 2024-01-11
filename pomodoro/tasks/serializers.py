from pomodoros.models import Pomodoro
from pomodoros.serializers import PomodoroCreateSerializer
from projects.serializers import ProjectBasicInfoSerializer
from rest_framework import serializers

from .models import Task


class TaskPomodoroCreateSerializer(serializers.ModelSerializer):
    """Task Create model Serializer"""

    pomodoro_count = serializers.IntegerField(max_value=42, min_value=1)
    # TODO: Pomodoro의 데이터도 같이 response할 수 있도록 필드 추가하기 231124
    # read_only와 write_only로 해결.
    # Task가 pmodoro를 역참조
    pomodoros = PomodoroCreateSerializer(many=True, read_only=True)

    # read_only와 write_only를 해도 반드시 fields에 정의해야 에러가 나지 않는다.
    # Task모델을 return하고 나서 to_representation 메소드에서 write_only, read_only를 확인해서
    # 클라이언트에게 데이터로 return할 field를 결정하기 때문에
    # class Meta에 지정하는 field는 옵션관계 없이 모두 포함시켜야 한다.
    class Meta:
        model = Task
        fields = ["id", "name", "priority", "due_date", "pomodoro_count", "pomodoros"]

    def create(self, validated_data):
        pomodoro_count = validated_data.get("pomodoro_count")
        # pomodoro_count = validated_data.pop("pomodoro_count")
        task = Task.objects.create(**validated_data)
        pomodoros = [Pomodoro(task=task) for _ in range(pomodoro_count)]
        Pomodoro.objects.bulk_create(pomodoros)

        return task


class TaskDetailSerializer(serializers.ModelSerializer):
    """Task Detail Serializer"""
    
    # pomodoro는 task detail을 get한 뒤.
    # 유저가 pomodoro_count부분을 누르면
    # task의 id를 사용해서 별도로 pomodoro list(pomodoro의 상세내용 포함)을 get하는 api를 사용할 것이므로
    # 여기에는 포함시키지 않는다.
    projects = ProjectBasicInfoSerializer(read_only=True)

    class Meta:
        model = Task
        fields = ["id", "due_date", "pomodoro_count", "projects"]
