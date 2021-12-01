class FileManager:

    def __init__(self, filename):
        self.__filename = filename
        print("__init__() of parent FileManager class has been called!")
    
    def __str__(self):
        obj_desc = "Instance of FileManager class. This class is used to read content from files.\n"
        obj_desc = obj_desc + "This instance reads from: '%s'" % self.__filename
        return obj_desc

    def get_line_at(self, num):
        file_1 = open(self.__filename)
        content = -1
        line_num = 0
        for line in file_1:
            if line_num == num:
                content = line
            line_num = line_num + 1
        file_1.close()
        if type(content) == str:
            return content[:-1]
        else:
            return content

    # q4    
    def get_filename(self):
        return self.__filename


class MemberFileManager(FileManager):
    
    # q6
    def get_participant_at(self,id_num):
        data = self.get_line_at(id_num)
        data_as_list = data.split(',')
        id = data_as_list[0]
        name = [data_as_list[1], data_as_list[2]]
        email = data_as_list[3]
        data_as_dict = {
            id:{
                "name": name,
                "email": email
            }
        }
        return data_as_dict
    
    # q4
    def __str__(self):
        description = "Instance of MemberFileManager class. This class is a child of the FileManager class and retrieves information about members from %s" % self.get_filename()
        return description


member_info = MemberFileManager("member_data.txt")
print(member_info)
print(member_info.get_participant_at(3))



