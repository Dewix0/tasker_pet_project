from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Task
from .serializers import TaskSerializer

class SortedTaskListView(APIView):

    def bubble_sort(self,tasks):
        task_array=list(tasks)
        n=len(task_array)
        
        for i in range(n - 1):
            for j in range(n - i - 1):
                if task_array[j].Deadline > task_array[j + 1].Deadline:
                    task_array[j], task_array[j + 1] = task_array[j + 1], task_array[j]
        
        return task_array
    

    PRIORITY_CHOICES = {"H": 1, "M": 2, "L": 3}

    def quick_sort(self, tasks):
        if len(tasks) <= 1:
            return tasks

        pivot = tasks[0] 
        left = [task for task in tasks[1:] if self.PRIORITY_CHOICES[task.Priority] <= self.PRIORITY_CHOICES[pivot.Priority]]
        right = [task for task in tasks[1:] if self.PRIORITY_CHOICES[task.Priority] > self.PRIORITY_CHOICES[pivot.Priority]]

        return self.quick_sort(left) + [pivot] + self.quick_sort(right)
    
    def get(self, request,sort_by):
        tasks = Task.objects.all()
        if sort_by == "deadline":
            sorted_tasks = self.bubble_sort(tasks)
        elif sort_by == "priority":
            sorted_tasks = self.quick_sort(list(tasks))
        else:
            return Response({"error": "Ошибка. Доступные параметры сортировки: deadline или priority"}, status=status.HTTP_400_BAD_REQUEST)

        serializer = TaskSerializer(sorted_tasks, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)