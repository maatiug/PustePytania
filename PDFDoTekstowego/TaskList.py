from TextParser import *
import Config

class Task:

    def __init__(self, from_pdf: str):
        self.conntent = from_pdf

    def __str__(self):
        return self.conntent

    @staticmethod
    def parse(from_pdf: str) -> str:
        """ private """
        raise NotImplementedError()


class TaskList:

    def __init__(self):
        self.tasks = []
        self.all_cnt = 0
        self.unique_cnt = 0

    def __str__(self):
        return self.print_result()

    def add_from_pdf_txt(self, text: str):
        """ public """
        parsering = TextParser(text)
        parsering.delete(TextParser.get_patterns(Config.DELETE_PATT))
        parsering.delete_head_lines(Config.DELETE_HEADLINES)

        for task_conn in parsering.split(Config.SPLIT_PATT):
            new_task = Task(task_conn)
            self.all_cnt += 1

            if self.is_unique(new_task):
                self.tasks.append(new_task)
                self.unique_cnt += 1

    def is_unique(self, new_task: Task) -> bool:
        """ private """
        raise NotImplementedError()

    def save_to_file(self, file_path: str):
        """ public """
        raise NotImplementedError()

    def print_result(self):
        """ private """
        raise NotImplementedError()
