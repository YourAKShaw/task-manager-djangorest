from task.serializers import CreateTaskSerializer, UpdateTaskSerializer


def validate_create_task_request_data(request_data):
    validation_result = {
        "success": True,
        "errors": None
    }
    validation = CreateTaskSerializer(data=request_data)
    if (validation.is_valid()):
        pass
    else:
        validation_result["success"] = False
        validation_result["errors"] = validation.errors
    return validation_result


def validate_update_task_request_data(request_data):
    validation_result = {
        "success": True,
        "errors": None
    }
    validation = UpdateTaskSerializer(data=request_data)
    if (validation.is_valid()):
        pass
    else:
        validation_result["success"] = False
        validation_result["errors"] = validation.errors
    return validation_result
