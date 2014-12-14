Feature: creating an extremely simple implementation of
         several Unix commands: ls, touch, and rm.

         As a user I wish to be able to maniuplate my files in my
         present directory

         Scenario: creating and deleting files using command 
         Given the command script
         When I run the command application succesfully
         Then I see the following
        |                   files                                       | 
        | Creating file...                                              |
        |Content of dir:  ['command_app.py', 'command.py']              |
        |Content of dir:  ['command_app.py', 'command.py', 'test_file'] |
        |File created.                                                  |
        |Deleting file...                                               |
        |Content of dir:  ['command_app.py', 'command.py', 'test_file'] |
        |Content of dir:  ['.test_file', 'command_app.py', 'command.py']|
        |File deleted.                                                  |