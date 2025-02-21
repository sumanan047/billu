# utils for dev only
import inspect
import os
import datetime


def log_call_stack(file_path):
    """
    Decorator function that logs the call stack of a decorated function to a file.

    Args:
        file_path (str): The path of the file to log the call stack.

    Returns:
        function: The decorated function.

    Example:
        @log_call_stack('/path/to/log.txt')
        def my_function(arg1, arg2):
            # Function implementation
            pass
    """
    def decorator(func):
        def wrapper(*args, **kwargs):
            with open(file_path, 'a') as file:
                timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                function_name = func.__name__
                arguments = ', '.join([repr(arg) for arg in args] + [f"{key}={repr(value)}" for key, value in kwargs.items()])
                log_message = f"{timestamp} - {function_name} - Arguments: {arguments}\n"
                file.write(log_message)
                file.write('=' * 50 + '\n')
                
                # Write the called function and its arguments to the log file
                # stack = inspect.stack()
                # for frame in stack[1:]:
                #     function = frame.function
                #     argo = frame.frame.f_locals
                #     arguments = '\n'.join([f"{key}={repr(value)}" for key, value in argo.items()])
                #     log_message = f"{timestamp} - {function} - Arguments: {arguments}\n"
                #     file.write(log_message)
                #     file.write('=' * 50 + '\n')
                    
            return func(*args, **kwargs)
        return wrapper
    return decorator


def delete_files_with_extensions(directory, extensions):
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            if any(file.endswith(extension) for extension in extensions):
                os.remove(file_path)
